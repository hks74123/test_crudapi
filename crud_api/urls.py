from django.contrib import admin
from django.urls import path
from crud_api.views import Student_data

urlpatterns = [
    path('allstudents/',Student_data.as_view(),name='allstudents'),
    path('allstudents/<int:pk>/',Student_data.as_view()),
]