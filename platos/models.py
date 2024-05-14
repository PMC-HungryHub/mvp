from djongo import models

class Plato(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    imagen = models.CharField(max_length=255)
    precio = models.IntegerField()
    tipo = models.CharField(max_length=50)
