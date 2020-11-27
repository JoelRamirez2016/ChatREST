from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from chatAPI.serializers import UserSerializer, MessageSerializer
from chatAPI.models import Message

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
