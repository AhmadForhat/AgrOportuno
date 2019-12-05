from django.shortcuts import render

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
