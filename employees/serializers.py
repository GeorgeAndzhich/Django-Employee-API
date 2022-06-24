from attr import field
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    models = Employee
    field = '__all__'