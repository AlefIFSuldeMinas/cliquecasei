from django.db import models

class ConviteCasamento(models.Model):
    NomeNoiva= models.CharField(max_length=100)
    NomeNoivo= models.CharField(max_length=100)
    DataCasamento = models.DateField()
    Capa = models.ImageField()
    FotoCasal = models.ImageField()
    Descricao = models.CharField(max_length=100)
    Endereco = models.CharField(max_length=100)
    Cidade = models.CharField(max_length=100)
    Estado  = models.CharField(max_length=100)
    Cep = models.CharField(max_length=100)
    ListaPresentes = models.CharField(max_length=100)
    IdUsuario = models.IntegerField(default=0)

class Convidados(models.Model):
    NomeConvidado = models.TextField(blank=True)
    Acompanhantes = models.TextField(blank=True)
    TelefoneConvidado = models.TextField(blank=True)
    Observacoes = models.TextField(blank=True)
    IdCasal = models.IntegerField(default=0)

