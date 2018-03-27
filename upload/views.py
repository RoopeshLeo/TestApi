# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response
from .serializers import FileSerializer,CollegeSerializer
from rest_framework import status
from .models import College
from . import serializers

class FileViewSet(APIView):
    parser_classes=(MultiPartParser,FormParser)
    def post(self,requset,*args,**kwargs):
        fs=FileSerializer(data=requset.data)
        if fs.is_valid():
            fs.save()
            return Response(fs.data,status=status.HTTP_201_CREATED)
        else:
            return Response(fs.errors,status=status.HTTP_400_BAD_REQUEST)
        
class CollegeViewSet(APIView):
    def post(self,requset,*args,**kwargs):
        fs=CollegeSerializer(data=requset.data)
        if fs.is_valid():
            fs.save()
            return Response(fs.data,status=status.HTTP_201_CREATED)
        else:
            return Response(fs.errors,status=status.HTTP_400_BAD_REQUEST)
        
class CollegeListViewSet(APIView):
    def get(self,request,pk=None,format=None):
        queryset=College.objects.all()        
        serializer=serializers.CollegeSerializer(queryset,many=True,context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
        

