from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'age', 'branch', 'email']
        read_only_fields = ['student_id']  # student_id is auto-generated, so it should be read-only