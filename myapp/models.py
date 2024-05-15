from django.db import models

class Plato(models.Model):
    
    id2= models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
