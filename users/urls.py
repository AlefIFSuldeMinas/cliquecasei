from django.urls import URLPattern, path
from . import views
urlpatterns = [
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('', views.loginDjango, name = 'login'),
    path('site/', views.site, name='site')
]