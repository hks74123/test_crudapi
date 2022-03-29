from functools import partial

from django.views import View
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import StudentSerializer
from crud_api.repositry import student_api

# Create your views here.

class Student_data(APIView):
    #Check if user is autheticated 
    permission_classes = (IsAuthenticated, )
    def get(self, request, pk=None):
        serializer = student_api.get_students_data(pk)
        return Response(serializer.data)

    def post(self, request, formate=None):
        serializer = student_api.post_students_data(request.data)
        if(serializer==True):
            return Response({'msg':'Data created sucessfully'})
        else:
            return Response(serializer)

    def patch(self, request, pk, formate=None):
        serializer = student_api.update_students_data(request.data, pk) 
        if(serializer == True):
            return Response({'msg':'Updation complete'})
        else:
            return Response(serializer)
    
    def delete(self, request, pk, formate=None):
        serializer = student_api.delete_student_data(pk)
        if(serializer == True):
            return Response({'msg':'deletion complete'})
        