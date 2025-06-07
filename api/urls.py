from django.urls import path, include

from . import views

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:student_id>/', views.studentDetailView),
]