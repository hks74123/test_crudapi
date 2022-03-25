from functools import partial

from django.views import View
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import StudentSerializer

# Create your views here.

class Student_data(APIView):
    #Check if user is autheticated 
    permission_classes = (IsAuthenticated, )
    def get(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    def post(self, request, formate=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created sucessfully'})
        return Response(serializer.errors)

    def patch(self, request, pk, formate=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Updation complete'})
        return Response(serializer.errors)
    
    def delete(self, request, pk, formate=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'deleted successfully'})
        