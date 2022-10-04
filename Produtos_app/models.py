from email.policy import default
from django.db import models

# Create your models here.

from django.contrib.auth.models import User #

class Produto(models.Model):
    foto = models.ImageField(upload_to='uploads/')
    #fotos
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)#related_name_padrao='produto_set'
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade = models.IntegerField(default=1)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    #cupom/promocao/evento
    

    class Meta:
        verbose_name = ("produto")
        verbose_name_plural = ("produtos")

    def __str__(self):
        return self.nome

