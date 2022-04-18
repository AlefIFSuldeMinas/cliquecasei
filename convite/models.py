from django.db import models

class ConviteCasamento(models.Model):
    Capa = models.ImageField(upload_to ='uploads/')
    NomeNoivos = models.TextField(max)
    DataCasamento = models.DateTimeField
    GaleriaId = models.IntegerField
    Descricao = models.TextField(400)
    Onde = models.TextField(max)
    ListaPresentes = models.TextField(max)