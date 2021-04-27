from django.shortcuts import render
from  .serializers import TaskSerializers
from rest_framework import viewsets
from .models import Task

class taskviewclass(viewsets.ModelViewSet):
    queryset  =Task.objects.all()
    serializer_class  = TaskSerializers

