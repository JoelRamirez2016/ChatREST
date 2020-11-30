from django.contrib.auth.models import User
from rest_framework import serializers
from chatAPI.models import Message


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializador de usuarios: heredara los metodos (ModelSerializer) 
    que seran utilizados como endpoints"""
    
    class Meta:
        model = User
        fields = ['id','password', 'username', 'email']

class MessageSerializer(serializers.ModelSerializer):
    """Serializador de mensaje: heredara los metodos (ModelSerializer) 
    que seran utilizados como endpoints"""

    class Meta:
        model = Message
        fields = ['id', 'content_img', 'content_txt','user_writer_id']
