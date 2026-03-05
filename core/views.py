from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job, Application, PlacementRecord


def home(request):
    return render(request, 'home.html')


# ✅ DASHBOARD (Admin + Student separation)
@login_required
def dashboard(request):

    # 🔥 If Admin → redirect to admin dashboard
    if request.user.is_superuser:
        return redirect('admin_dashboard')

    # 👨‍🎓 Student dashboard
    applications = Application.objects.filter(student=request.user)

    total = applications.count()
    selected = applications.filter(status="Selected").count()
    rejected = applications.filter(status="Rejected").count()

    return render(request, 'student_dashboard.html', {
        'applications': applications,
        'total': total,
        'selected': selected,
        'rejected': rejected
    })


# ✅ ADMIN DASHBOARD
@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('dashboard')

    applications = Application.objects.all()

    return render(request, 'admin_dashboard.html', {
        'applications': applications
    })


# ✅ JOB LIST (Student)
@login_required
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})


# ✅ APPLY JOB
@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    # Prevent admin from applying
    if request.user.is_superuser:
        return redirect('admin_dashboard')

    if request.method == 'POST':
        resume = request.FILES.get('resume')

        Application.objects.create(
            student=request.user,
            job=job,
            resume=resume,
            status='Pending'   # 🔥 Changed from Applied to Pending
        )

        return redirect('dashboard')

    return render(request, 'apply.html', {'job': job})


# ✅ SELECT APPLICATION (Admin only)
@login_required
def select_application(request, id):
    if not request.user.is_superuser:
        return redirect('dashboard')

    application = get_object_or_404(Application, id=id)
    application.status = "Selected"
    application.save()

    return redirect('admin_dashboard')


# ✅ REJECT APPLICATION (Admin only)
@login_required
def reject_application(request, id):
    if not request.user.is_superuser:
        return redirect('dashboard')

    application = get_object_or_404(Application, id=id)
    application.status = "Rejected"
    application.save()

    return redirect('admin_dashboard')


# ✅ PLACEMENT REPORT
@login_required
def placement_report(request):
    records = PlacementRecord.objects.all()
    return render(request, 'placement_report.html', {'records': records})