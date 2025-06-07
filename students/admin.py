from django.contrib import admin
from .models import Student
# Register your models here.

# This will register student model to the admin dashboard
admin.site.register(Student)