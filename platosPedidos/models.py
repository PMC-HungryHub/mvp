from djongo import models
from pedidos.models import Pedido
from platos.models import Plato

class PlatoPedido(models.Model):
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=255)
    pedido = models.ForeignKey(Pedido, related_name='pedido', on_delete=models.CASCADE)
    plato = models.ForeignKey(Plato, related_name='plato_pedido', on_delete=models.CASCADE)