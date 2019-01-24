from rest_framework import serializers
from .models import MyUser

class MyUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password', 'following')
