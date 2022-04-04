from django.urls import URLPattern, path
from .views import HomeView
urlpatterns = [
    path('',HomeView.as_view(), name = 'home'),
]