from django import forms
from Agrodoce.models import Cadastro

class CadastroForm(forms.ModelForm):
    class Meta : 
        model = Cadastro
        fields = [
            'nome_completo',
            'email',
            'categoria',
            'senha',
        ]