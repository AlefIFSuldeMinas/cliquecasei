from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    NomeUsuario = models.TextField(blank=True)
    Endereco = models.TextField(blank=True)
    Celular = models.TextField(blank=True)
    Cidade = models.TextField(blank=True)
    Estado = models.TextField(blank=True)
    Cep = models.TextField(blank=True)
    Bairro = models.TextField(blank=True)
