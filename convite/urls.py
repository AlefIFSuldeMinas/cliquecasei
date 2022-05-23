from django.urls import path
from . import views
 
urlpatterns = [
    path('CadastroConvite/', views.CadastroConvite, name = 'CadastroConvite'),
]