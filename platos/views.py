from django.shortcuts import redirect, render
from django.conf import settings

def lista_platos(request):
   restaurantes = settings.DB["Restaurantes"]
   documento = restaurantes.find_one({"nombre": "Restaurante de los Alpes"})
   platos = documento["platos"]

   if request.method=="POST":
      idPlato = int(request.POST.get("idPlato"))
      # Buscar el plato en la lista de platos
      plato = None
      for p in platos:
         if p["id2"] == idPlato:
            plato = p
            break
      if plato:
         restaurantes.update_one({"nombre": "Restaurante de los Alpes"},{"$push": {"pedido": plato}})

   return render(request, 'lista_platos.html', {'platos': platos})

""" 
def pedir_plato(request, plato_id):
    pedidos = settings.DB["Pedidos"].find()
    pedidos.insert_one({"nombre": plato_nombre, "id": plato_id })
    return HttpResponse("¡Plato pedido! ID del plato: {}".format(plato_id))
 """