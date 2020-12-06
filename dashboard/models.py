from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model


class Ususario(models.Model):
    primeiro_nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=11)


class Cliente(models.model):
    telefone = models.CharField(max_length=11)
    usuario = models.OneToOneField(User)


class Endereco(models.Model):
    telefone_contato = models.CharField(max_length=11)
    cep = models.CharField(max_length=8)
    bairro = models.CharField(max_length=120)
    rua = models.CharField(max_length=120)
    numero = models.CharField(max_length=10)
    informacao_adicional = models.CharField(max_length=240)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Produto(models.Model):
    produto_nome = models.CharField(max_length=240)
    valor = models.FloatField()
    descricao = models.CharField()


class ImagemProduto(models.Model):
    imagem_produto = models.ImageField()
    imagem_descricao = models.CharField(max_length=480)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)


class ItemPedido(models.Model):
    quantidade = models.IntegerField()
    valor_total = models.CharField()
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE)


class Pedido(models.Model):
    data = models.DateField()
    valor_total = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    itempedido = models.ForeignKey(ItemPedido, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
