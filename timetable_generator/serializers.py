from rest_framework import serializers
from .models import Student,Login,Faculty,HOD,Department,Semester


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields='__all__'

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields='__all__'

class HODSerializer(serializers.ModelSerializer):
    class Meta:
        model=HOD
        fields='__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Semester
        fields='__all__'

