from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework import permissions
from chatAPI.serializers import UserSerializer, MessageSerializer
from chatAPI.models import Message
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .forms import CreateUserForm

def chat_index(request):
    messages = Message.objects.all()
    users = User.objects.all()
    return render(request, template_name='index.html', context={
        'messages': messages,
        'users': users
        })

def register_user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, template_name='register.html', context={
        'form': form
        })

def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('psw')
        user = authenticate(request, username=username, password=password)
        print(username,password,user)
        if user is not None:
            login(request,user)
            return redirect('chat_view')

    return render(request, template_name='login.html', context={

        })
        
def logout_user(request):
    logout(request)
    return redirect('login')


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
    search_fields = ['content_txt']
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
