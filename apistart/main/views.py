from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, TaskSerializer
from .models import Task


class UserRegistrationView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'form.html'
    success_url = reverse_lazy('main:login')


class UserLoginView(LoginView):
    template_name = 'form.html'
    success_url = reverse_lazy('main:main')


class UserLogoutView(LogoutView):
    http_method_names = ['get', 'post']
    next_page = reverse_lazy('main:main')
    template_name = 'main/logout.html'


def main(request):
    return render(request, 'main/main.html')


class UserAPI(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    @login_required
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TaskAPI(ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer


from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate

class CustomLoginAPIView(APIView):
    def post(self, request, format=None):
        data = request.data
        
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if not user:
            return Response({"error": "Неверное имя пользователя или пароль."}, status=400)
        
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({"token": token.key, "user_id": user.pk})