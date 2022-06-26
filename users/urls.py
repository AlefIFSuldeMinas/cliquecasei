from django.urls import URLPattern, path
from . import views
urlpatterns = [
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('', views.loginDjango, name = 'login'),
    path('sair/', views.sair, name='sair'),
    path("Perfil/", views.Perfil, name ="Perfil"),
    path('edicao/', views.edicao, name = 'edicao'),
]