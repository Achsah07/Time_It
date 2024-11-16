from django.contrib import admin
from. models import Student
from. models import Login
from. models import HOD
from. models import Faculty
from. models import Department
from. models import Semester

# Register your models here.
admin.site.register(Student)
admin.site.register(Login)
admin.site.register(HOD)

admin.site.register(Faculty)
admin.site.register(Department)
