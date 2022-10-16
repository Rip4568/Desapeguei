from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    #CHAVES ESTRANGEIRAS
    usuario = models.OneToOneField(User, related_name='perfil', on_delete=models.CASCADE)
    #CAMPOS
    foto = models.ImageField(upload_to='uploads/',blank=True,null=True)
    nome = models.CharField(max_length=255,blank=True,null=True)
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

