from django.db import models
from django.contrib.auth.models import User

class RoleChoices(models.TextChoices):
    ADMIN="Admin","Admin"
    STUDENT="Student","Student"
    FACULTY="Faculty","Faculty"
    HOD="hod","hod"

class Login(models.Model):  
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=40)
    role = models.CharField(max_length=40,choices=RoleChoices.choices)

class Student(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=40)
    department = models.CharField(max_length=40)
    mobile = models.BigIntegerField(null=False)
    login_id = models.OneToOneField(Login, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=40)
    department = models.CharField(max_length=40)
    mobile = models.BigIntegerField(null=False)
    login_id = models.OneToOneField(Login, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class HOD(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=40)
    department = models.CharField(max_length=40)
    mobile = models.BigIntegerField(null=False)
    login_id = models.OneToOneField(Login, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Department(models.Model):
    dept_name = models.CharField(max_length=40)
    dept_id=models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Semester(models.Model):
    sem_name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

