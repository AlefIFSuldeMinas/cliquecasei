from django.db import models

class ConviteCasamento(models.Model):
    Capa = models.ImageField(upload_to ='uploads/')
    NomeNoivos = models.CharField(max)
    DataCasamento = models.DateTimeField
    GaleriaId = models.IntegerField
    Descricao = models.CharField(max)
    Onde = models.CharField(max)
    ListaPresentes = models.CharField(max)