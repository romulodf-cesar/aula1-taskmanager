# renderização da página
from django.shortcuts import render, redirect
from .forms import CategoriaForm, TarefaForm
from textblob import TextBlob
from .models import Tarefa


def nova_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tarefas')
    else:
        form = CategoriaForm()  # BUG CORRIGIDO: era CategoriaForm(request.POST)
    return render(request, 'todo/nova_categoria.html', {'form': form})


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


def traduzir_para_ingles(texto):
    """Tenta traduzir com googletrans; retorna texto original em caso de falha."""
    try:
        from googletrans import Translator
        translator = Translator()
        resultado = translator.translate(texto, src='pt', dest='en')
        # BUG CORRIGIDO: era TextBlob(traducao) — faltava .text
        return resultado.text
    except Exception:
        return texto  # fallback: usa português mesmo


def executar_nlp_raiz(texto):
    if not texto or not texto.strip():
        return "Sem Feedback", 0.0

    texto_en = traduzir_para_ingles(texto)
    blob = TextBlob(texto_en.text)  # BUG CORRIGIDO: era TextBlob(texto_en) — faltava .text
    polaridade = blob.sentiment.polarity

    # Limiares mais granulares (corrigido de binário para 4 faixas)
    if polaridade >= 0.3:
        sentimento = "Altamente Positivo / Construtivo"
    elif polaridade > 0:
        sentimento = "Levemente Positivo"
    elif polaridade <= -0.2:
        sentimento = "Negativo / Necessita de Atenção"
    else:
        sentimento = "Neutro / Orientação Técnica"

    return sentimento, round(polaridade, 4)


def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'todo/listar_tarefas.html', {'tarefas': tarefas})