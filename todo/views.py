from django.shortcuts import render
from .forms import CategoriaForm

def nova_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = CategoriaForm(request.POST)
    return render(request,'todo/nova_categoria.html',{'form':form})
