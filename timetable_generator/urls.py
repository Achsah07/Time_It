from django.urls import path,include
from.import views
urlpatterns = [
   path('',views.index),
#login
   path('login/',views.login_view.as_view()),
#student
   path('studentregistration/',views.student_reg.as_view()),
   path('viewStudents/',views.view_students.as_view()),
   path('studentlogin/<int:id>',views.student_login.as_view()),
   path('updatestudent/<int:id>',views.update_student.as_view()),
   path('deletestudent/<int:id>',views.delete_student.as_view()),

#faculty
   path('facultyregistration/',views.faculty_reg.as_view()),
   path('viewfaculty/',views.view_faculty.as_view()),
   path('facultylogin/<int:id>',views.faculty_login.as_view()),
   path('updatefaculty/<int:id>',views.update_faculty.as_view()),
   path('deletefaculty/<int:id>',views.delete_faculty.as_view()),
#hod
   path('hodregistration/',views.hod_reg.as_view()),
   path('viewhod/',views.view_hod.as_view()),
   path('hodlogin/<int:id>',views.hod_login.as_view()),
   path('updatehod/<int:id>',views.update_hod.as_view()),
   path('deletehod/<int:id>',views.delete_hod.as_view()),
#department
   path('departmentregistration/',views.department_reg.as_view()),
   path('viewDepartment/',views.view_department.as_view()),
   path('updatedepartment/<int:id>',views.update_department.as_view()),
   path('deletedepartment/<int:id>',views.delete_department.as_view()),
#semester
   path('semesterregistration/',views.semester_reg.as_view()),
   path('viewsemester/',views.view_semester.as_view()),
   path('deletesemester/<int:id>',views.delete_semester.as_view()),
#major
]