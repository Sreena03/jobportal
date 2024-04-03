from django.shortcuts import render
from rest_framework import authentication,permissions
from api.serializer import Login,Userserializer,Jobserializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from Myapp.models import Job
from rest_framework import status

# Create your views here.

class Jobviewsetview(ViewSet):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):
        qs = Job.objects.all()
        serializer = Jobserializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)
    
    def create(self,request,*args,**kwargs):
        serializer = Jobserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        qs = Job.objects.get(id=id)
        serializer = Jobserializer(qs)
        return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)

class Signup(APIView):
    def post(self,request,*args,**kwargs):
        serializer = Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data)

        else:
            return Response(data = serializer.errors)
        
