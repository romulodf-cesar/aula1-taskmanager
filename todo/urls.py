from django.urls import path
from .views  import nova_categoria,nova_tarefa


urlpatterns=[
    path('categoria/',nova_categoria,name='categoria'),
    path('tarefa/',nova_tarefa,name='nova_tarefa')
]