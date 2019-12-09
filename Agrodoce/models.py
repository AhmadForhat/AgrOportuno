from django.db import models

# Create your models here.

class Cadastro(models.Model):
    categoria_cadastro =[
        ('Agricultor','Agricultor'),
        ('Lojista','Lojista'),
    ]

    nome_completo = models.CharField(max_length=140)
    email = models.EmailField()
    categoria = models.CharField(max_length=10,choices = categoria_cadastro)
    senha = models.CharField(max_length = 8)

    def __str__ (self):
        return self.nome