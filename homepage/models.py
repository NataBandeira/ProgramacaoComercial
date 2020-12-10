from django.contrib.auth.models import User
from django.db import models

class Cliente(models.Model):
    telefone = models.CharField(max_length=11)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Endereco(models.Model):
    telefone_contato = models.CharField(max_length=11)
    cep = models.CharField(max_length=8)
    bairro = models.CharField(max_length=120)
    rua = models.CharField(max_length=120)
    numero = models.CharField(max_length=10)
    informacao_adicional = models.CharField(max_length=240)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

