from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from.serializers import StudentSerializer,LoginSerializer,FacultySerializer,HODSerializer,DepartmentSerializer,SemesterSerializer
from rest_framework.response import Response
from rest_framework import status
from . models import Student
from . models import Login,Faculty,HOD,Department,Semester
# Create your views here.
def index(request):
    return HttpResponse("he he")
    
class student_reg(GenericAPIView):
    def get_serializer_class(self):
        return StudentSerializer

    def post(self,request):

        login_id=""
        name=request.data.get('name')
        email=request.data.get('email')
        mobile=request.data.get('mobile')
        password=request.data.get('password')
        department=request.data.get('department')
        role='Student'

        if not name or not email or not mobile or not password or not department:
            return Response({'message': 'All fields are required'},status=status.HTTP_400_BAD_REQUEST,)

        if Student.objects.filter(email=email).exists():
            return Response({'message': 'Duplicate Emails are not allowed'},status=status.HTTP_400_BAD_REQUEST,)

        elif Student.objects.filter(mobile=mobile).exists():
            return Response({'message': 'Number already found'},status=status.HTTP_400_BAD_REQUEST,)

        login_serializer=LoginSerializer(data={'email':email,'password':password,'role':role})
        print(login_serializer)
        if login_serializer.is_valid():
            l=login_serializer.save()
            login_id=l.id

        else:
            return Response({'message':'Login Failed'},status=status.HTTP_400_BAD_REQUEST,)

        student_serializer=StudentSerializer(

        data={
            'name':name,
            'email':email,
            'mobile':mobile,
            'password':password,
            'department':department,
            'role':role,
            'login_id':login_id})

        if student_serializer.is_valid():
            student_serializer.save()
            return Response({'message':'Registration Successfull'},status=status.HTTP_200_OK,)

        else:
            return Response({'mmesage':'Registration Failed'},status=status.HTTP_400_BAD_REQUEST,)



class login_view(GenericAPIView):
    serializer_class=LoginSerializer

    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')

        logreg=Login.objects.filter(email=email,password=password)
        if(logreg.count()>0):
            read_serializers=LoginSerializer(logreg,many=True)

            for i in read_serializers.data:
                login_id=i['id']
                role=i['role']

                register_data=Student.objects.filter(login_id=login_id).values()
                for i in register_data:
                    name=i['name']

            return Response({'data':read_serializers.data,'success':1,'message':'Logged in Successfully'},status=status.HTTP_200_OK,)
        else:
            return Response({'message':'Login Failed'},status=status.HTTP_400_BAD_REQUEST,)


class faculty_reg(GenericAPIView):
    def get_serializer_class(self):
        return FacultySerializer

    def post(self,request):

        login_id=""
        name=request.data.get('name')
        email=request.data.get('email')
        mobile=request.data.get('mobile')
        password=request.data.get('password')
        department=request.data.get('department')
        role='Faculty'

        if not name or not email or not mobile or not password or not department:
            return Response({'message': 'All fields are required'},status=status.HTTP_400_BAD_REQUEST,)

        if Faculty.objects.filter(email=email).exists():
            return Response({'message': 'Duplicate Emails are not allowed'},status=status.HTTP_400_BAD_REQUEST,)

        elif Faculty.objects.filter(mobile=mobile).exists():
            return Response({'message': 'Number already found'},status=status.HTTP_400_BAD_REQUEST,)

        login_serializer=LoginSerializer(data={'email':email,'password':password,'role':role})
        print(login_serializer)
        if login_serializer.is_valid():
            l=login_serializer.save()
            login_id=l.id

        else:
            return Response({'message':'Login Failed'},status=status.HTTP_400_BAD_REQUEST,)

        faculty_serializer=FacultySerializer(

        data={
            'name':name,
            'email':email,
            'mobile':mobile,
            'password':password,
            'department':department,
            'role':role,
            'login_id':login_id})

        if faculty_serializer.is_valid():
            faculty_serializer.save()
            return Response({'message':'Registration Successfull'},status=status.HTTP_200_OK,)

        else:
            return Response({'message':'Registration Failed'},status=status.HTTP_400_BAD_REQUEST,)


class hod_reg(GenericAPIView):
    def get_serializer_class(self):
        return HODSerializer

    def post(self,request):

        login_id=""
        name=request.data.get('name')
        email=request.data.get('email')
        mobile=request.data.get('mobile')
        password=request.data.get('password')
        department=request.data.get('department')
        role='HOD'

        if not name or not email or not mobile or not password or not department:
            return Response({'message': 'All fields are required'},status=status.HTTP_400_BAD_REQUEST,)

        if HOD.objects.filter(email=email).exists():
            return Response({'message': 'Duplicate Emails are not allowed'},status=status.HTTP_400_BAD_REQUEST,)

        elif HOD.objects.filter(mobile=mobile).exists():
            return Response({'message': 'Number already found'},status=status.HTTP_400_BAD_REQUEST,)
        


        login_serializer=LoginSerializer(data={'email':email,'password':password,'role':role})
        print(login_serializer)
        if login_serializer.is_valid():
            l=login_serializer.save()
            login_id=l.id

        else:
            return Response({'message':'Login Failed'},status=status.HTTP_400_BAD_REQUEST,)

        hod_serializer=HODSerializer(

        data={
            'name':name,
            'email':email,
            'mobile':mobile,
            'password':password,
            'department':department,
            'role':role,
            'login_id':login_id})

        if hod_serializer.is_valid():
            hod_serializer.save()
            return Response({'message':'Registration Successfull'},status=status.HTTP_200_OK,)

        else:
            return Response({'message':'Registration Failed'},status=status.HTTP_400_BAD_REQUEST,)
        

class view_students(GenericAPIView):
            serializer_class=StudentSerializer

            def get(self,request):
                student=Student.objects.all()
                if student.count()>0:
                    serializerstd=StudentSerializer(student,many=True)
                    return Response({'data':serializerstd.data,'message':'Data fetched','success':True},status=status.HTTP_200_OK)
                else:
                    return Response({'data':'no data available'},status=status.HTTP_400_BAD_REQUEST)
                
class view_hod(GenericAPIView):
            serializer_class=HODSerializer

            def get(self,request):
                hod=HOD.objects.all()
                if hod.count()>0:
                    serializershod=HODSerializer(hod,many=True)
                    return Response({'data':serializershod.data,'message':'Data fetched','success':True},status=status.HTTP_200_OK)
                else:
                    return Response({'data':'no data available'},status=status.HTTP_400_BAD_REQUEST)
                
class view_faculty(GenericAPIView):
            serializer_class=FacultySerializer

            def get(self,request):
                faculty=Faculty.objects.all()
                if faculty.count()>0:
                    serializerflty=FacultySerializer(faculty,many=True)
                    return Response({'data':serializerflty.data,'message':'Data fetched','success':True},status=status.HTTP_200_OK)
                else:
                    return Response({'data':'no data available'},status=status.HTTP_400_BAD_REQUEST)
                
class student_login(GenericAPIView):
            serializer_class=StudentSerializer

            def get(self,request,id):
                student=Student.objects.get(pk=id)
                serializerstd=StudentSerializer(student)
                return Response(serializerstd.data)
            
class faculty_login(GenericAPIView):
            serializer_class=FacultySerializer

            def get(self,request,id):
                faculty=Faculty.objects.get(pk=id)
                serializerflty=FacultySerializer(faculty)
                return Response(serializerflty.data)
            
class hod_login(GenericAPIView):
            serializer_class=HODSerializer

            def get(self,request,id):
                hod=HOD.objects.get(pk=id)
                serializerhod=HODSerializer(hod)
                return Response(serializerhod.data)
            
class update_student(GenericAPIView):
            serializer_class=StudentSerializer

            def put(self,request,id):
                student=Student.objects.get(pk=id)
                serializerstd=StudentSerializer(instance=student,data=request.data,partial=True)

                if serializerstd.is_valid():
                    serializerstd.save()
                    return Response({'data':serializerstd.data,'message':'user updated successfully','success':True},status=status.HTTP_200_OK)
                
                return Response(serializerstd.errors,status=status.HTTP_400_BAD_REQUEST)
            
class update_faculty(GenericAPIView):
            serializer_class=FacultySerializer

            def put(self,request,id):
                faculty=Faculty.objects.get(pk=id)
                serializerflty=FacultySerializer(instance=faculty,data=request.data,partial=True)

                if serializerflty.is_valid():
                    serializerflty.save()
                    return Response({'data':serializerflty.data,'message':'user updated successfully','success':True},status=status.HTTP_200_OK)
                
                return Response(serializerflty.errors,status=status.HTTP_400_BAD_REQUEST)    

class update_hod(GenericAPIView):
            serializer_class=HODSerializer

            def put(self,request,id):
                hod=HOD.objects.get(pk=id)
                serializerhod=HODSerializer(instance=hod,data=request.data,partial=True)

                if serializerhod.is_valid():
                    serializerhod.save()
                    return Response({'data':serializerhod.data,'message':'user updated successfully','success':True},status=status.HTTP_200_OK)
                
                return Response(serializerhod.errors,status=status.HTTP_400_BAD_REQUEST)       

class delete_student(GenericAPIView):
            serializer_class=StudentSerializer

            def delete(self,request,id):
                student=Student.objects.get(pk=id)
                student.delete()
                return Response('successfully deleted')  
            
class delete_faculty(GenericAPIView):
            serializer_class=FacultySerializer

            def delete(self,request,id):
                faculty=Faculty.objects.get(pk=id)
                faculty.delete()
                return Response('successfully deleted')  
            
class delete_hod(GenericAPIView):
            serializer_class=HODSerializer

            def delete(self,request,id):
                hod=HOD.objects.get(pk=id)
                hod.delete()
                return Response('successfully deleted') 

  
            
class department_reg(GenericAPIView):
    def get_serializer_class(self):
        return DepartmentSerializer 
    
    def post(self,request):

       dept_name=request.data.get('dept_name')
       dept_id=request.data.get('dept_id')

       dept_serializer=DepartmentSerializer(

       data={
            'dept_name':dept_name,
            'dept_id':dept_id,})

       if dept_serializer.is_valid():
            dept_serializer.save()
            return Response({'message':'Registration Successfull'},status=status.HTTP_200_OK,)

       else:
            return Response({'message':'Registration Failed'},status=status.HTTP_400_BAD_REQUEST,)
       
class view_department(GenericAPIView):
            serializer_class=DepartmentSerializer

            def get(self,request):
                department=Department.objects.all()
                if department.count()>0:
                    serializerdept=DepartmentSerializer(department,many=True)
                    return Response({'data':serializerdept.data,'message':'Data fetched','success':True},status=status.HTTP_200_OK)
                else:
                    return Response({'data':'no data available'},status=status.HTTP_400_BAD_REQUEST)
        
class update_department(GenericAPIView):
            serializer_class=DepartmentSerializer

            def put(self,request,id):
                department=Department.objects.get(pk=id)
                serializerdept=DepartmentSerializer(instance=department,data=request.data,partial=True)

                if serializerdept.is_valid():
                    serializerdept.save()
                    return Response({'data':serializerdept.data,'message':'user updated successfully','success':True},status=status.HTTP_200_OK)
                
                return Response(serializerdept.errors,status=status.HTTP_400_BAD_REQUEST)
            
class delete_department(GenericAPIView):
            serializer_class=DepartmentSerializer

            def delete(self,request,id):
                department=Department.objects.get(pk=id)
                department.delete()
                return Response('successfully deleted')    

class semester_reg(GenericAPIView):
    def get_serializer_class(self):
        return SemesterSerializer 
    
    def post(self,request):

       sem_name=request.data.get('sem_name')

       sem_serializer=SemesterSerializer(

       data={
            'sem_name':sem_name,
            })

       if sem_serializer.is_valid():
            sem_serializer.save()
            return Response({'message':'Registration Successfull'},status=status.HTTP_200_OK,)

       else:
            return Response({'message':'Registration Failed'},status=status.HTTP_400_BAD_REQUEST,)
       
class view_semester(GenericAPIView):
            serializer_class=SemesterSerializer

            def get(self,request):
                semester=Semester.objects.all()
                if semester.count()>0:
                    serializersem=SemesterSerializer(semester,many=True)
                    return Response({'data':serializersem.data,'message':'Data fetched','success':True},status=status.HTTP_200_OK)
                else:
                    return Response({'data':'no data available'},status=status.HTTP_400_BAD_REQUEST)    


class delete_semester(GenericAPIView):
            serializer_class=SemesterSerializer

            def delete(self,request,id):
                semester=Semester.objects.get(pk=id)
                semester.delete()
                return Response('successfully deleted')    
