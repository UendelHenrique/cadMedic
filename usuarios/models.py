from django.db import models

class Medico(models.Model):
    nome_medico = models.CharField(max_length=200)
    especializacao = models.CharField(max_length=200)
    crm = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
