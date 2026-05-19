from django import forms
from .models import Categoria,Tarefa

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


class TarefaForm(forms.ModelForm):
    class Meta:
            model = Tarefa
            fields = ['titulo', 'descricao', 'categoria','feedback_professor']
            widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'feedback_superior': forms.Textarea(attrs={'class': 'form-control', 'rows':2}), }