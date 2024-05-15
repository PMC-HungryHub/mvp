from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

def listar_pedidos(request):
    pedidos = settings.DB["Pedidos"].find()
    return render(request, "lista_pedidos.html", {"pedidos": pedidos})