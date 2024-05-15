import pymongo
import sys
from django.shortcuts import redirect, render
from .models import Plato


client = pymongo.MongoClient ('mongodb://hungryhub84:fFgkg89qCuK1KJ3a@ac-t4pykdt-shard-00-00.pbi899i.mongodb.net:27017,ac-t4pykdt-shard-00-01.pbi899i.mongodb.net:27017,ac-t4pykdt-shard-00-02.pbi899i.mongodb.net:27017/?ssl=true&replicaSet=atlas-654uob-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0')
db = client.HungryHub




def lista_platos(request):
   restaurantes= db["Restaurantes"]
   documento = restaurantes.find_one({"nombre": "Restaurante de los Alpes"})
   platos=documento["platos"]



   if request.method=="POST":
        
        pedidos = db["Pedidos"].find()
        

        if "boton" in request.POST:

            nombre= request.POST["boton"]
            pedidos = db["Pedidos"]
            pedidos.insert_one({"nombre": nombre})

   return render(request, 'lista_platos.html', {'platos': platos})

""" 
def pedir_plato(request, plato_id):
    client = pymongo.MongoClient ('mongodb://hungryhub84:fFgkg89qCuK1KJ3a@ac-t4pykdt-shard-00-00.pbi899i.mongodb.net:27017,ac-t4pykdt-shard-00-01.pbi899i.mongodb.net:27017,ac-t4pykdt-shard-00-02.pbi899i.mongodb.net:27017/?ssl=true&replicaSet=atlas-654uob-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0')
    db = client.HungryHub
    pedidos = db["Pedidos"].find()
    pedidos.insert_one({"nombre": plato_nombre, "id": plato_id })


    return HttpResponse("¡Plato pedido! ID del plato: {}".format(plato_id))
 """