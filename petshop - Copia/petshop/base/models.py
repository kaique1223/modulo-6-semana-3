from django.db import models

# Create your models here.
class contatom(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

class reservam(models.Model):
    nome_do_pet = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    dia_da_reserva = models.CharField(max_length=50)
    observaçao = models.TextField(verbose_name="observaçao",blank=True)
