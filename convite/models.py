from django.db import models

class ConviteCasamento(models.Model):
    NomeNoiva= models.CharField(max_length=100)
    NomeNoivo= models.CharField(max_length=100)
    DataCasamento = models.DateTimeField()
    Capa = models.ImageField()
    FotoCasal = models.ImageField()
    Descricao = models.CharField(max_length=100)
    Endereco = models.CharField(max_length=100)
    Cidade = models.CharField(max_length=100)
    Estado  = models.CharField(max_length=100)
    Cep = models.CharField(max_length=100)
    ListaPresentes = models.CharField(max_length=100)
    IdUsuario = models.IntegerField(default=0)

