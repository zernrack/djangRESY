# from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from students.models import Student
from .serializers import StudentSerializer

from employees.models import Employee
from .serializers import EmployeeSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def studentsView(request):
   if request.method == 'GET':
      students = Student.objects.all()
      serializer = StudentSerializer(students, many=True)

      return Response(serializer.data, status=status.HTTP_200_OK)

   elif request.method == 'POST':
      serializer = StudentSerializer(data=request.data) # data=request.data indicates that the serializer should use the data from the request
      if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # If the request method is GET, return the student record
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # If the request method is PUT, update the student record
    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # If the request method is DELETE, delete the student record
    if request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # If the request method is not GET, PUT, or DELETE, return a 405 Method Not Allowed response
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class EmployeesView(APIView):
    # GET method to retrieve all employees
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True) #Many=True indicates that the serializer should expect a list of objects
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST method to create a new employee
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data) # data=request.data indicates that the serializer should use the data from the request
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)