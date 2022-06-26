from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from convite.models import Convidados, ConviteCasamento
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

def edicao(request):
    User.objects.filter(pk=request.user.id).update(
        NomeUsuario = request.POST.get('NomeUsuario'),
        username = request.POST.get('Email'),
        Endereco = request.POST.get('Endereco'),
        Celular = request.POST.get('Celular'),
        Cidade = request.POST.get('Cidade'),
        Estado = request.POST.get('Estado'),
        Cep = request.POST.get('Cep'),
        Bairro = request.POST.get('Bairro'),
        )
    usuario = User.objects.filter(id=request.user.id).get()
    contexto = {
         'usuario': usuario
    }
    return render(request, 'users/index.html', contexto)

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
            return redirect('Perfil')
        else:
            context['password_error'] = "Credenciais inválidas!"
            return render(request, 'users/login.html', context)

def sair(request):
    return render(request, 'users/login.html')

def Acessar(request):
    return render(request, 'users/index.html')

def site(request):
    if request.user.is_authenticated:
        return HttpResponse('Logado')
    else:
        return HttpResponse('Erroooou!')

def Perfil(request):
    usuario = User.objects.filter(id=request.user.id).get()
    convitesDeCasamento = ConviteCasamento.objects.all().filter(IdUsuario=request.user.id)
    convidados = Convidados.objects.all().filter(IdCasal=request.user.id)
    contexto = {
      'usuario': usuario,
      'convites': convitesDeCasamento,
      'convidados': convidados
    }
    return render(request, "users/index.html", contexto)
