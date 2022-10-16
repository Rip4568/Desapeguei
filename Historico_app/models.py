from django.db import models
from Perfil_app.models import Perfil
from Produtos_app.models import Produto

#o historico será criado se e somente se a compra for bem sucedida
class Historico(models.Model):
    #Chaves estrangeiras
    comprador = models.ForeignKey(Perfil,related_name="comprador", on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Perfil, related_name="vendedor",on_delete=models.CASCADE)
    #Campos
    produto = models.ForeignKey(Produto, related_name='produto', on_delete=models.CASCADE,blank=True,null=True)
    quantidade_comprada = models.PositiveIntegerField()
    acao = models.CharField(choices=(('Comprar','Comprar'),('Vender','Vender')), max_length=7,blank=False,null=False)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("historico")
        verbose_name_plural = ("historicos")

    def __str__(self):
        return self.acao