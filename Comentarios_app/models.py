from django.db import models

from Perfil_app.models import Perfil
from Produtos_app.models import Produto

class Comentario(models.Model):
    comentado_por = models.OneToOneField(Perfil, on_delete=models.CASCADE, related_name="comentario")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="comentarios")
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.comentario

    @property
    def estrela(self):
        return self.produto.ratings.get(id=self.comentado_por.id)