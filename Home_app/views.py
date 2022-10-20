import decimal

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView
from Comentarios_app.forms import ComentarioManualForm
from Comentarios_app.models import Comentario

from Historico_app.models import Historico
from Perfil_app.models import Perfil
from Produtos_app.forms import ProdutoManualForm
from Produtos_app.models import Categoria, Produto

TEMPLATE_HISTORICO_PUBLICACAO_PATH = 'Home_app/hitorico-publicacao.html'
TEMPLATE_HISTORICO_PATH = 'Home_app/historicos.html'
class HomeTemplateView(TemplateView):
    template_name = "Home_app/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["produtos"] = Produto.objects.filter(disponivel=True).order_by('-data_de_publicacao')#lista de produtos masi recentes
        #talvez trocar o a chave para produtos_recentes
        context["produtos_mais_votados"] = Produto.objects.filter(disponivel=True).order_by('ratings')
        return context
    

class ShopTemplateView(ListView):
    model = Produto
    paginate_by = 9
    template_name = "Home_app/shop.html"
    context_object_name = 'produtos'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["produtos"] = Produto.objects.filter(disponivel=True)
        return context
    
    
    def post(self,request):
        context = dict()
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            if self.request.POST.get('mais-recentes') is not None:
                context["produtos"] = Produto.objects.filter(disponivel=True).order_by('-data_de_publicacao')
            else:
                context['produtos'] = Produto.objects.filter(disponivel=True).order_by('-ratings')
        return render(self.request,"Home_app/shop.html",context=context)

class DetailTemplateView(DetailView):
    pk_url_kwarg = 'id_produto'
    template_name = "Home_app/detail.html"
    model = Produto
    context_object_name = 'produto'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["produtos_sugestao"] = Produto.objects.all().order_by('-ratings')[0:5]
        context["form"] = ComentarioManualForm
        context["comentarios"] = Comentario.objects.filter(produto=self.get_object())
        context["ja_comentou"] = Comentario.objects.filter(produto=self.get_object(), comentado_por=self.request.user.perfil).exists()
        return context

    def post(self,request,*args, **kwargs):
        quantidade_comprada_produto = int(self.request.POST.get("quantidade_a_ser_comprada"))
        #produto = self.get_object()#sera que essse metodo não é funcional ?
        produto = Produto.objects.get(pk=self.get_object().pk)
        comprador = self.request.user.perfil
        vendedor = Perfil.objects.get(pk=produto.publicado_por.pk)
        compra_total = decimal.Decimal(quantidade_comprada_produto) * produto.preco
        if produto.quantidade >= int(quantidade_comprada_produto):#se a quantidade for maior ou igual comprada
            Historico.objects.create(
            comprador=comprador,
            vendedor=produto.publicado_por,
            produto=produto,
            quantidade_comprada=int(quantidade_comprada_produto),
            preco=produto.preco,
            acao='Comprar',
            )
            produto.quantidade -= quantidade_comprada_produto
            if produto.quantidade == 0:
                produto.disponivel = False
            produto.save()
            vendedor.saldo += compra_total
            vendedor.save()
            comprador.saldo -= compra_total
            comprador.save()
        else:
            return HttpResponse("Tentativa de burlar o sistema detectatdo!, quantidade a ser comprada : {} , quantidade disponivel : {}".format(quantidade_comprada_produto, produto.quantidade))
        return redirect(reverse('Home_app:Detail',args=[self.get_object().id]))

    

class ProdutoCategoriaListView(ListView):
    model = Categoria
    template_name = ".html"


class ContactTemplteView(TemplateView):
    template_name = "Home_app/contact.html"

class CheckoutTemplateView(TemplateView):
    template_name = "Home_app/checkout.html"

class CartTemplateView(TemplateView):
    template_name = "Home_app/cart.html"

class VenderProdutoView(TemplateView):  
    template_name = "Home_app/vender-produto.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(f'{self.request.POST}')
        usuario = self.request.user
        context["formmanual"] = ProdutoManualForm
        context["usuario"] = usuario
        context["prateleira"] = Produto.objects.filter(publicado_por=usuario.perfil).order_by('-data_de_publicacao')[0:5]
        return context
    
    def post(self,*args, **kwargs):
        formulario = ProdutoManualForm(self.request.POST)
        if formulario.is_valid():
            foto = self.request.POST.get('foto')
            nome = self.request.POST.get('nome')
            preco = self.request.POST.get('preco')
            descricao = self.request.POST.get('descricao')
            quantidade = self.request.POST.get('quantidade')
            categoria = self.request.POST.get('categoria')
            Produto.objects.create(
                publicado_por=self.get_context_data().get('usuario').perfil,
                foto=foto,
                nome=nome,
                preco=preco,
                descricao=descricao,
                quantidade=quantidade,
                categoria=Categoria.objects.get(slug=categoria),
            )
            formulario = ProdutoManualForm()#limpar os campos
        return redirect(reverse('Home_app:vender_produto'))
        
class HistoricoPublicacaoCompletoListView(ListView):
    template_name = TEMPLATE_HISTORICO_PUBLICACAO_PATH
    paginate_by = 10
    model = Produto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['historico_publicacao'] = Produto.objects.filter(publicado_por=self.request.user.perfil)#funcionando sem isso ?
        return context
    
    
class HistoricosListView(ListView):
    template_name = TEMPLATE_HISTORICO_PATH
    paginate_by = 10
    model = Historico
    context_object_name = 'historicos'


class CategoriaFiltragemDetailView(DetailView):
    model = Categoria
    template_name = "Home_app/shop.html"
    pk_url_kwarg = 'categoria_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["produtos"] = Produto.objects.filter(categoria=self.get_object())
        return context
    
def criar_comentario(request):
    print("{}".format(request.POST))
    comentario_novo = Comentario.objects.create(
        comentado_por=Perfil.objects.get(pk=request.user.perfil.pk),
        produto=Produto.objects.get(pk=request.POST.get("produto")),
        comentario=request.POST.get('comentario')
    ).save()
    return redirect(reverse('Home_app:Detail',args=(comentario_novo.produto.pk)))


def populate(request):
    categorias = ["Tecnologia","Remedios","Moveis","Eletrodomesticos","Construção"]
    for categoria in categorias:
        Categoria.objects.create(categoria=categoria,slug=categoria)
    return HttpResponseRedirect(reverse("Home_app:Home"))

