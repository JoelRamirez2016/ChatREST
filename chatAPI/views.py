from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from chatAPI.serializers import UserSerializer, MessageSerializer, LoginsLogSerializer
from chatAPI.models import Message, LoginsLog
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


def chat_index(request):
    messages = Message.objects.all()
    return render(request, template_name='index.html', context={'messages': messages} )

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Message.objects.all().order_by('id')
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['user_writer_id']
    search_fields = ['content']
    permission_classes = [permissions.IsAuthenticated]
    
class LoginsLogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LoginsLog.objects.all().order_by('id')
    serializer_class = LoginsLogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id','date']
    permission_classes = [permissions.IsAuthenticated]

    # def post(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         content = serializer.validated_data.get('content')
    #         return Response({'msg' : 'guardando'})
    #     else:
    #         return Respone(
    #             serializer.errors,
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
