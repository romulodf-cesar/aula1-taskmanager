from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        widgets ={
            'nome':forms.TextInput(attrs={'class':'form-control',
             'placeholder':'Ex: Java, Python, Cloud, IA, Ciência de Dados',
             'style':'max-width:370px;'               
            })
        }