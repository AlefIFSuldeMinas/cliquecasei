from django.urls import path
from . import views
 
urlpatterns = [
    path('CadastroConvite/', views.CadastroConvite, name = 'CadastroConvite'),
    path("ConviteCasamentoVM/<codigoId>/", views.ConviteCasamentoVM, name ="ConviteCasamentoVM"),
    path("CadastrarConvidado", views.CadastrarConvidado, name ="CadastrarConvidado"),
]