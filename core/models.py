from django.db import models
from django.contrib.auth.models import AbstractUser


# ✅ Custom User Model
class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('STUDENT', 'Student'),
        ('EMPLOYER', 'Employer'),
        ('OFFICER', 'Placement Officer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


# ✅ Company Model (Separate & Correct)
class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ✅ Job Model
class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ✅ Application Model
class Application(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'STUDENT'})
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.student.username} - {self.job.title}"


# ✅ Placement Record
class PlacementRecord(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'STUDENT'})
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    salary = models.CharField(max_length=100)
    placed_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} placed at {self.company.name}"