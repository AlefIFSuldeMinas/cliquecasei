from django.urls import URLPattern, path
from . import views
urlpatterns = [
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('login/', views.login, name = 'login'),
    path('site/', views.site, name='site')
]