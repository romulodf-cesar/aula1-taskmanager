# renderização da página
from django.shortcuts import render,redirect
# importa a classe CategoriaForm
from .forms import CategoriaForm,TarefaForm
from mtranslate import translate
from textblob import TextBlob

#função para cadastrar a nova categoria
def nova_categoria(request): # request - requisição (client/server)
    # se condição então ... verdadeira
    if request.method == 'POST': # informa que o usuário quer cadastrar
        form = CategoriaForm(request.POST) # carrega os dados no obj form
        if form.is_valid(): #verifica se o form é válido
            form.save() # insere o form no banco de dados (commit)

    else: # resultado falso da condição
        form = CategoriaForm(request.POST) # recarrega o formulário atual
    # retorna a renderização da página passando os dados do form {}
    return render(request,'todo/nova_categoria.html',{'form':form})


def nova_tarefa(request):
    form = TarefaForm()
    if request.method == 'POST':
            form = TarefaForm(request.POST)
            if form.is_valid():
                tarefa = form.save(commit=False)
                sentimento, score = executar_nlp_raiz(tarefa.feedback_professor)
                tarefa.analise_sentimento = sentimento
                tarefa.score_polaridade = score
                tarefa.save()
                return redirect('listar_tarefas')
            
    return render(request, 'todo/nova_tarefa.html', {'form': form})

def executar_nlp_raiz(texto):
    if not texto:
        return "Sem Feedback", 0.0
    
    try:
        # Traduz o texto do português (pt) para o inglês (en)
        texto_en = translate(texto, 'en', 'pt')
        blob = TextBlob(texto_en)
    except Exception:
        # Caso a tradução falhe (ex: sem internet), usa o texto original
        blob = TextBlob(texto)
        
    polaridade = blob.sentiment.polarity
    
    if polaridade > 0.3:
        sentimento = "Altamente Positivo / Construtivo"
    elif polaridade < -0.2:
        sentimento = "Negativo / Necessita de Atenção"
    else:
        sentimento = "Neutro / Orientação Técnica"
        
    return sentimento, polaridade

def listar_tarefas(request):
    return render(request,'todo/listar_tarefas.html')