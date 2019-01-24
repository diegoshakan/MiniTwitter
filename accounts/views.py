from django.shortcuts import render
from .models import MyUser
from .serializers import MyUserModelSerializer
from rest_framework import viewsets
# Create your views here.

class MyUserModelViewSet(viewsets.ModelViewSet):
    serializer_class = MyUserModelSerializer
    queryset = MyUser.objects.all().order_by('-username')