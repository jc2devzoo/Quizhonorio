from django.shortcuts import render
from .models import *
from django.http import JsonResponse

def home(request):
    temas =  Tema.objects.all()
    context = {'temas' : temas}
    return render(request, 'home.html', context)

def api_perg(request, id):
    prim_perguntas = Pergunta.objects.filter(tema = id)[:20]
    perguntas = []
    
    for prim_pergunta in prim_perguntas:
        pergunta = {}
        pergunta['pergunta'] = prim_pergunta.pergunta
        pergunta['resposta'] = prim_pergunta.resposta
        opcoes = []
        opcoes.append(prim_pergunta.prim_res)
        opcoes.append(prim_pergunta.sec_res)
        if prim_pergunta.ter_res !='':
            opcoes.append(prim_pergunta.ter_res)
        
        if  prim_pergunta.quar_res != '':  
            opcoes.append(prim_pergunta.quar_res)
            
        pergunta['opcoes'] = opcoes
        
        perguntas.append(pergunta)
        
    return JsonResponse(perguntas , safe=False)
        
        

def get_quiz(request, id):
        context = {'id': id}
        return render(request , 'quiz.html', context)