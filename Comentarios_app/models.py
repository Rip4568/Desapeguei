from django.db import models

from Perfil_app.models import Perfil
from Produtos_app.models import Produto

class Comentario(models.Model):
    comentado_por = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    comentario = models.TextField()

    def __str__(self):
        return self.comentado_por
    