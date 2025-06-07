from django.urls import path, include

from . import views

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:student_id>/', views.studentDetailView),

    path('employees/', views.EmployeesView.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view()),
]