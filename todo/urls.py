from django.urls import path
from .views  import nova_categoria


urlpatterns=[
    path('categoria/',nova_categoria,name='categoria')
]