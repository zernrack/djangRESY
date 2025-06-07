# from django.http import JsonResponse
from django.http import Http404
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

class EmployeeDetailView(APIView):
    # Helper method to get an employee object by ID
    def get_object(self, employee_id):
        try:
            return Employee.objects.get(pk=employee_id)
        except Employee.DoesNotExist:
            raise Http404

    # GET method to retrieve a specific employee by ID
    def get(self, request, employee_id):
        employee = self.get_object(employee_id) # Use the helper method to get the employee object
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT method to update a specific employee by ID
    def put(self, request, employee_id):
        employee = self.get_object(employee_id)

        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE method to delete a specific employee by ID
    def delete(self, request, employee_id):
       employee = self.get_object(employee_id)

       employee.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)