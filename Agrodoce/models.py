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


class Produto(models.Model):
    tipo_de_produto = [
        ('Maquina','Maquina'),
        ('Legumes','Legumes'),
        ('Frutas','Frutas'),
    ]
    tipo_de_paagmento = [
        ('avista','Pagamento á vista'),
        ('P2','Parcelado em 2x'),
        ('P3','Parcelado em 3x'),
    ]

    nome_produto = models.CharField(max_length=50)
    preco = models.DecimalField(decimal_places=2,max_digits=1000000,default=50)
    imagem = models.ImageField(upload_to='')


    def __str__(self):
        return self.nome