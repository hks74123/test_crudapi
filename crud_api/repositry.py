from rest_framework.response import Response

from .models import *
from .serializers import StudentSerializer

# api to get data
class student_api():
    def get_students_data(pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu)
            return serializer
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return serializer

    def post_students_data(data):
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return True
        return serializer.errors

    def update_students_data(data,pk):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return True
        return Response(serializer.errors)

    def delete_student_data(pk):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return True
