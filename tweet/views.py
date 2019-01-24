from django.shortcuts import render
from rest_framework import viewsets
from .models import Tweet
from .serializers import TweetModelSerializer

# Create your views here.

class TweetModelViewSet(viewsets.ModelViewSet):
    serializer_class = TweetModelSerializer
    queryset = Tweet.objects.all()
