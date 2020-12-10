from django.db import models
from django.contrib.auth.models import User


class Produto(models.Model):
    produto_nome = models.CharField(max_length=240)
    valor = models.FloatField()
    descricao = models.CharField(max_length=480)


class ImagemProduto(models.Model):
    imagem_produto = models.ImageField(upload_to='images/',  blank=True)
    imagem_descricao = models.CharField(max_length=480)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
