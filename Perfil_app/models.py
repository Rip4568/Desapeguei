from email.policy import default
from random import choices
from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, related_name='usuario', on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='uploads/',blank=True,null=True)
    nome = models.CharField(max_length=255,blank=True,null=True)
    ingressou = models.DateTimeField(auto_now_add=False)
    saldo = models.DecimalField(max_digits=9, decimal_places=2, default=100_000)

    class Meta:
        verbose_name = ("perfil")
        verbose_name_plural = ("perfis")

    def __str__(self):
        return f"{self.usuario}"
