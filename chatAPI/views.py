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
    """ metodo para renderizar la vista del chat """
    messages = Message.objects.all()
    users = User.objects.all().order_by('-last_login').exclude(last_login = None)
    return render(request, template_name='index.html', context={
        'messages': messages,
        'users': users
        })

def register_user(request):
    """ metodo para la creacion de usuarios """
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
    """ metodo para el logout de usuarios: el login del viewSet se mantiene """

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
    """ metodo para el logout de usuarios: el logout del viewSet se mantiene """
    logout(request)
    return redirect('login')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint para el control de usuarios mediante urls
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint para el control de mensajes mediante urls
    """
    queryset = Message.objects.all().order_by('id')
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    # filter_fields = {
    #     'id': ['gte', 'lte']
    # }
    filterset_fields = ['user_writer_id','id']
    search_fields = ['content_txt']
    permission_classes = [permissions.IsAuthenticated]
    