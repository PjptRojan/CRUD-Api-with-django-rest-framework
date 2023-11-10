from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only= True) - to validate single field
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        read_only_fields = ['name', 'roll']