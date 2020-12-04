from django.db import models

class Ususario(models.Model):
    primeiro_nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=11)
