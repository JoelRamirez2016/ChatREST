from django.contrib.auth.models import User
from rest_framework import serializers
from chatAPI.models import Message


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','url', 'username', 'email']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content','user_writer_id']

class LoginsLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'user_id','date']
