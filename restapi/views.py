from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializer import TestSerializers
from rest_framework import generics

global data;
data = ["test"]

# Create your views here.
class Data(APIView):

    def get(self,request,format=None):
        message = {
            'Response':200,
            'Message': 'Welcome to Django Rest API',
        }
        return Response(message)

    def post(self,request,format=None):
        getdata = request.data
        name = getdata.get('name',None)
        data.append(name)
        message = {
            'Response':200,
            'Message': 'Welcome to Django Rest API',
            'data':data,
        }
        return Response(message)    

class TestData(generics.CreateAPIView):
    serializer_class = TestSerializers
    def create(self,request,*args,**kwargs):
        try:
            zip= request.data.get('zip')
            city= request.data.get('city')
            age= request.data.get('age')
            
            return super().create(request,*args,**kwargs)

        except Exception as e:
            return Response(
                {
                    "Message":"Failed"
                }
            )    