from django.shortcuts import redirect, render
from django.conf import settings

def lista_platos(request):
   restaurantes = settings.DB["Restaurantes"]
   documento = restaurantes.find_one({"nombre": "Restaurante de los Alpes"})
   platos = documento["platos"]

   if request.method=="POST":
        pedidos = settings.DB["Pedidos"].find()
        if "boton" in request.POST:
            nombre= request.POST["boton"]
            pedidos = settings.DB["Pedidos"]
            pedidos.insert_one({"nombre": nombre})

   return render(request, 'lista_platos.html', {'platos': platos})

""" 
def pedir_plato(request, plato_id):
    pedidos = settings.DB["Pedidos"].find()
    pedidos.insert_one({"nombre": plato_nombre, "id": plato_id })
    return HttpResponse("¡Plato pedido! ID del plato: {}".format(plato_id))
 """