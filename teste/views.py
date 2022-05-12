from django.shortcuts import render
from .models import *
from django.http import JsonResponse

def home(request):
    temas =  Tema.objects.all()
    context = {'temas' : temas}
    return render(request, 'home.html', context)
