# marketing/models.py

from django.db import models


class Campanha(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    arquivo = models.FileField(upload_to='campanhas/')

    def __str__(self):
        return self.nome

class MaterialApoio(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    arquivo = models.FileField(upload_to='materiais_apoio/')

    def __str__(self):
        return self.nome
