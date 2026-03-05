from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Dashboard (Admin + Student auto separation)
    path('dashboard/', views.dashboard, name='dashboard'),

    # Student Features
    path('jobs/', views.job_list, name='job_list'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),

    # Admin Dashboard
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Admin Actions
    path('select/<int:id>/', views.select_application, name='select_application'),
    path('reject/<int:id>/', views.reject_application, name='reject_application'),

    # Placement Report
    path('placement-report/', views.placement_report, name='placement_report'),
]