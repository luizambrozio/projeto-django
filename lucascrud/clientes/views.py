from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Cliente
from .forms import ClienteForm

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def create_cliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    
    return render(request, 'clientes-form.html', {'form': form})

def update_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('lista_clientes')

    return render(request, 'clientes-form.html', {'form': form, 'cliente': cliente})

def delete_cliente(request, id):
    cliente = Cliente.objects.get(id=id)

    if form.method == 'POST':
        form.delete()
        return redirect('lista_clientes')

    return render(request, 'delete-cliente.html', {'cliente': cliente})