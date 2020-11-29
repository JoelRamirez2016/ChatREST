from django.contrib.auth.models import User
from rest_framework import serializers
from chatAPI.models import Message


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','password', 'username', 'email']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content_img', 'content_txt','user_writer_id']
