from importlib.metadata import requires
from django.contrib.auth import login, get_user_model
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from users.models import User


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


def loginDjango(request):
    context = {}

    if request.method == "GET":
        return render(request, 'users/login.html', context)
    else:
        Email = request.POST.get('Email')
        Senha = request.POST.get('Senha')

        if(Email == "" or Senha == ""):
            context['password_error'] = "Não deixe nenhum campo de login em branco!"
            return render(request, 'users/login.html', context)

        user = authenticate(username=Email, password=Senha)

        if user:
            login(request, user)
            return render(request, 'convite/cadastro_convite.html')
        else:
            context['password_error'] = "Credenciais inválidas!"
            return render(request, 'users/login.html', context)


def site(request):
    if request.user.is_authenticated:
        return HttpResponse('Logado')
    else:
        return HttpResponse('Erroooou!')


class HomeView(TemplateView):
    template_name = 'users/index.html'
