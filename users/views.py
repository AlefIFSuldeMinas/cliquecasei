from importlib.metadata import requires
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginDjango
from users.models import User

def cadastro(request):
    if request.method == "GET":
        return render(request, 'users/cadastro_usuario.html')
    else:
        NomeUsuario = request.POST.get('NomeUsuario')
        Email = request.POST.get('Email')
        Senha = request.POST.get('Senha')
        user = User.objects.create_user(username=NomeUsuario,email=Email,password=Senha)
        user.save()
        return HttpResponse(NomeUsuario)

def login(request):
    if request.method == "GET":
        return render(request, 'users/login.html')
    else:
        NomeUsuario = request.POST.get('NomeUsuario')
        Senha = request.POST.get('Senha')
        user = authenticate(username=NomeUsuario, password=Senha)
        if user:
            loginDjango(request, user)
            return HttpResponse("Logado com sucesso!")
        else:
            return HttpResponse('Senha errada')

def site(request):
    if request.user.is_authenticated:
        return HttpResponse('Logado')
    else:
        return HttpResponse('Erroooou!')
        
class HomeView(TemplateView):
    template_name = 'users/index.html'
