from itertools import zip_longest
from django import forms
from django.forms import NumberInput, Widget
from .models import Categoria, Produto

def lista_de_categorias() -> list:
    if Categoria.objects.exists():
        try:
            categorias = [(categoria.categoria, categoria.categoria) for categoria in Categoria.objects.all()]
        except:
            return [('error','error')]
    else:
        categorias = [('Sem_Categoria','Sem_Categoria')]
        return categorias
    return categorias
        

class ProdutoManualForm(forms.Form):
    #foto = models.ImageField(upload_to='uploads/',blank=True,null=True)
    foto = forms.ImageField(
        label="Foto do produto* (apenas uma)",
        allow_empty_file=False,
        required=False,
        )
    
    #nome = models.CharField(max_length=255)
    nome = forms.CharField(

        required=True,
        label="Nome do Produto* ",
        widget=forms.TextInput(
        attrs={
            "placeholder":"digite o nome do produto aqui",
            "class":"form-control",
            "id":"id_nome_produto_input",
            
            }
        )
    )
    #preco = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    preco = forms.DecimalField(
        #code
        required=True,
        max_digits=6,
        min_value=0,
        decimal_places=2,
        label="Preço do produto *",
        initial="",
        widget=forms.NumberInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite o preço do produto..."
            }
        )
    )
    
    #descricao = models.TextField(blank=True,null=True)
    descricao = forms.CharField(
        label_suffix="",
        required=False,
        label="",
        widget=forms.Textarea(
            attrs={
                "rows":6,
                "placeholder":"Digite a descrição do produto (opcional)...",
                "class":"form-control"
            }
        )
    )

    #quantidade = models.PositiveIntegerField(default=1)
    quantidade = forms.IntegerField(
        max_value=999,
        min_value=0,
        required=True,
        label="Quantidade do produto",
        widget=forms.NumberInput(
            attrs={
                "placeholder":"Digite a quantidade de produtos a serem vendidos",
                "class":"form-control",
            }
        )
    )
    
    #categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    categoria = forms.ChoiceField(
        label="Categoria do produto",
        required=True,
        choices=lista_de_categorias(),
        #widget=forms.QUAL_WIDGET_VAI_AQUI
    )
    
    #disponivel = models.BooleanField(default=True) #talvez nao sera necessario
    #o campo disponivel sera manipulado automaticamente pelo sistema

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = (
            "foto",
            "nome",
            "preco",
            "descricao",
            "quantidade",
            "categoria",
        )
        widgets = {
            "nome":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Digite o nome do produto aqui",
            }),
            "preco":forms.NumberInput(attrs={
                "class":"form-control",
                "placeholder":"Digite o preço do seu produto (por item)",
            }),
            "descricao":forms.Textarea(attrs={
                "class":"form-control",
                "placeholder":"Digite a descrição do produto aqui ...",
                "style":"height: 146px",
            }),
            "quantidade":forms.NumberInput(attrs={
               "class":"form-control",
               "placeholder":"Digite a quantidade disponivel para venda...",
            }),
        }
