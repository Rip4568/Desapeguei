from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import MinValueValidator
from django.db import models
from star_ratings.models import Rating

from Perfil_app.models import Perfil


class Imagens(models.Model):
    foto = models.ImageField(upload_to='uploads/')
    class Meta:
        verbose_name = ("imagens")
        verbose_name_plural = ("imagenss")

    def __str__(self):
        return self.foto

class Categoria(models.Model):
    categoria = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    imagem = models.ImageField(upload_to='uploads/',null=True,blank=True)
    imagem_static_url = models.CharField(max_length=128,default="img/no_image.png")
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.slug = self.categoria
        
    @property
    def produtos_relacionados_quantidade(self):
        return self.produto_set.all().count()
    
    def __str__(self):
        return self.categoria


class Produto(models.Model):  
    publicado_por = models.ForeignKey(Perfil, on_delete=models.CASCADE, default=1,null=False,blank=False)
    foto = models.ImageField(upload_to='uploads/',blank=True,null=True)
    fotos = models.ForeignKey(Imagens, on_delete=models.DO_NOTHING,blank=True,null=True)
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    descricao = models.TextField(blank=True,null=True)#descricao do produto
    informacao = models.TextField(blank=True,null=True)
    data_de_publicacao = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    quantidade = models.PositiveIntegerField(default=1)
    ratings = GenericRelation(Rating, related_query_name='produto')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    disponivel = models.BooleanField(default=True)
    vendido = models.BooleanField(default=False,null=True,blank=True)
    
    
    def atualizar_quantidade(self,quantidade):
        self.quantidade += quantidade

    def valor_total(self):
        return self.quantidade * self.preco
    class Meta:
        verbose_name = ("produto")
        verbose_name_plural = ("produtos")

    def __str__(self):
        return self.nome