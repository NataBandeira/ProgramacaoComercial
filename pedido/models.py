from django.db import models
from loja.models import *
from homepage.models import Endereco

class ItemPedido(models.Model):
    quantidade = models.IntegerField()
    valor_total = models.FloatField()
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE)


class Pedido(models.Model):
    data = models.DateField()
    valor_total = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    itempedido = models.ForeignKey(ItemPedido, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
