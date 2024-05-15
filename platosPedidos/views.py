from django.shortcuts import render
from django.conf import settings

def mostrar_carrito(request):
    pedidos= settings.DB["Pedidos"].find()
    return render(request, "carrito.html", {"pedidos": pedidos})
