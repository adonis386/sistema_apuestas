# filepath: /c:/Users/Telvenshop/Desktop/sistema_apuestas/sistema_apuestas/core/urls.py
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]