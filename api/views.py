from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def studentsView(request):
   students = {
         "id": 1,
         "name": "John Doe",
         "age": 20,
   }

   return JsonResponse(students)