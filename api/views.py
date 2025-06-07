from django.http import JsonResponse
from django.shortcuts import render
from students.models import Student

# Create your views here.
def studentsView(request):
   students = Student.objects.all()

   students_list = list(students.values())
   print(students)

   return JsonResponse(students_list, safe=False)