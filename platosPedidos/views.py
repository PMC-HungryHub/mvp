from django.shortcuts import render
import pymongo

def carrito(request):

    client = pymongo.MongoClient ('mongodb://hungryhub84:fFgkg89qCuK1KJ3a@ac-t4pykdt-shard-00-00.pbi899i.mongodb.net:27017,ac-t4pykdt-shard-00-01.pbi899i.mongodb.net:27017,ac-t4pykdt-shard-00-02.pbi899i.mongodb.net:27017/?ssl=true&replicaSet=atlas-654uob-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0')
    db = client.HungryHub
    pedidos= db["Pedidos"].find()

    return render(request, "carrito.html", {"pedidos": pedidos})
