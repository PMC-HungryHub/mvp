import pymongo
import sys
from django.shortcuts import redirect, render
from .models import Plato


client = pymongo.MongoClient ('mongodb://hungryhub84:fFgkg89qCuK1KJ3a@ac-t4pykdt-shard-00-00.pbi899i.mongodb.net:27017,ac-t4pykdt-shard-00-01.pbi899i.mongodb.net:27017,ac-t4pykdt-shard-00-02.pbi899i.mongodb.net:27017/?ssl=true&replicaSet=atlas-654uob-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0')
db = client.HungryHub
platos = db["Platos"].find()

print(platos)


def lista_platos(request):

    return render(request, 'lista_platos.html', {'platos': platos})



"""def pedir_plato(request, plato_id):
    client = pymongo.MongoClient ('mongodb://hungryhub84:fFgkg89qCuK1KJ3a@ac-t4pykdt-shard-00-00.pbi899i.mongodb.net:27017,ac-t4pykdt-shard-00-01.pbi899i.mongodb.net:27017,ac-t4pykdt-shard-00-02.pbi899i.mongodb.net:27017/?ssl=true&replicaSet=atlas-654uob-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0')
    db = client.HungryHub
    pedidos = db["Pedidos"].find()
    pedidos.insert_one({"nombre": plato_nombre, "id": plato_id })


    return HttpResponse("¡Plato pedido! ID del plato: {}".format(plato_id))
"""
