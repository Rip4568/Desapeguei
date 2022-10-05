from email.policy import default
from random import choices
from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from Produtos_app.models import Produto

class Historico(models.Model):
    acao = models.CharField(choices=(('Comprar','Comprar'),('Vender','Vender')), max_length=7,blank=False,null=False)

    class Meta:
        verbose_name = ("historico")
        verbose_name_plural = ("historicos")

    def __str__(self):
        return self.name


class Perfil(models.Model):
    #CHAVES ESTRANGEIRAS
    usuario = models.OneToOneField(User, related_name='perfil', on_delete=models.CASCADE)
    historico = models.ForeignKey(Historico, related_name='historicos', on_delete=models.CASCADE,blank=True,null=True)
    #CAMPOS
    foto = models.ImageField(upload_to='uploads/',blank=True,null=True)
    nome_completo = models.CharField(max_length=255,blank=True,null=True)
    ingressou = models.DateTimeField(auto_now_add=True)
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=100_000,blank=False,null=False)
    
    #MetaData
    class Meta:
        verbose_name = ("perfil")
        verbose_name_plural = ("perfis")
        
    #metodos
    def incrementar_saldo(self,valor):
        self.saldo += valor
        self.save()
        return self.saldo
    
    def decrementar_saldo(self,valor):
        #fazer a verificação de decrementação aqui ?
        self.saldo -= valor
        self.save()
        return self.saldo

    def __str__(self):
        return f"{self.usuario}"
