from django.shortcuts import render
from Agrodoce.forms import CadastroForm
from Agrodoce.models import *

# Create your views here.

# def inicio(request):
#     return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def contato(request):
    return render(request , 'contato.html')

def login(request):
    return render(request , 'login.html')

def sobre(request):
    return render(request , 'sobre.html')

def cadastro(request):
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        form.save()
        context = {
            'msg': 'Cadastro realizado com sucesso'
        }
        return render (request , 'cadastro.html', context)
    context = {
        'formulario' : form
    }
    return render (request , 'cadastro.html' , context)