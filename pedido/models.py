from django.db import models
from loja.models import *
from homepage.models import Endereco
from loja.models import *

class Pedido(models.Model):
    data = models.DateField()
    valor_total = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=None, null=True)
    item_pedido = models.ForeignKey(Produto, on_delete=models.CASCADE)
    endereco_entrega = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True)

    @property
    def imagem_produto(self):
        return ImagemProduto.objects.filter(produto=self.item_pedido)[0].imagem_produto
    