from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def students(request):
    students = [
        {"name": "John Doe", "age": 20, "grade": "A"},
        {"name": "Jane Smith", "age": 22, "grade": "B"},
        {"name": "Alice Johnson", "age": 21, "grade": "C"},
        {"name": "Bob Brown", "age": 23, "grade": "A"},
    ]
    return HttpResponse(students)