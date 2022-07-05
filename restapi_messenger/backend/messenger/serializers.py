from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'username', 'avatar', ]


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        # fields = ['title', 'users', 'is_direct', 'last_message']
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['author', 'created', 'text', ]
