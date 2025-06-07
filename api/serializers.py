from rest_framework import serializers
from students.models import Student
from employees.models import Employee

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'age', 'branch', 'email']
        read_only_fields = ['student_id']
        # student_id is auto-generated, so it should be read-only


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','first_name', 'last_name', 'designation'] # Include fields that want to be serialized
        read_only_fields = ['id']  # id is auto-generated, so it should be read-only