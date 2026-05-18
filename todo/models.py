from django.db import models
#from django.contrib.auth.models import User

# tabela de categoria
# tabela de tarefas

class Categoria(models.Model):
    nome = models.CharField(max_length=100,
                             verbose_name="Nome da Categoria")
    def __str__(self):
        return self.nome
    
class Tarefa(models.Model):
    # dados da tarefa
    titulo = models.CharField(max_length=200,verbose_name="Titulo da Tarefa",blank=True,null=True)
    descricao = models.TextField(verbose_name="Descriçaõ da Tarefa",blank=True,null=True)
    concluida = models.BooleanField(default=False,verbose_name="Concluída")
    # relacionamento 1:NOTE - 
    # SET_NULL ele apaga o vínculo e apenas isso. Ele deixa o campo da categoria das tarefas "vazio";
    categoria = models.ForeignKey(Categoria,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="Categoria")

    # dados da PLN (processamento de linguagem natural)
    # IA para análise de sentimentos

    feedback_professor = models.TextField(verbose_name="Feedback Professor",blank="True",null="True")
    analise_sentimento = models.CharField(max_length=50,verbose_name="Análise de Sentimento",blank=True,null=True)
    score_polaridade = models.FloatField(default=0.0,verbose_name="Score de Polaridade")

    def __str__(self):
        return self.titulo + self.score_polaridade
  


