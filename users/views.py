from importlib.metadata import requires
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginDjango
from users.models import User
import logging


def cadastro(request):
    if request.method == "GET":
        return render(request, 'users/cadastro_usuario.html')
    else:
        NomeUsuario = request.POST.get('NomeUsuario')
        Email = request.POST.get('Email')
        Senha = request.POST.get('Senha')
        Endereco = request.POST.get('Endereco')
        Celular = request.POST.get('Celular')
        Cidade = request.POST.get('Cidade')
        Estado = request.POST.get('Estado')
        Cep = request.POST.get('Cep')
        Bairro = request.POST.get('Bairro')

        user = User.objects.create_user(
            username=Email,
            password=Senha,
            NomeUsuario=NomeUsuario,          
            Endereco=Endereco,
            Celular=Celular,
            Cidade=Cidade,
            Estado=Estado,
            Cep=Cep,
            Bairro=Bairro
        )
        user.save()
        return render(request, 'users/login.html')


def login(request):
    if request.method == "GET":
        return render(request, 'users/login.html')
    else:
        Email = request.POST.get('Email')
        Senha = request.POST.get('Senha')
        print(Senha, Email)
        user = authenticate(username=Email, password=Senha)

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
