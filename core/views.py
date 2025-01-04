# filepath: /c:/Users/Telvenshop/Desktop/sistema_apuestas/sistema_apuestas/core/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'core/user.html')
