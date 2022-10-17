from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, TemplateView

from Historico_app.models import Historico
from Produtos_app.forms import ProdutoManualForm
from Produtos_app.models import Categoria, Produto

TEMPLATE_HISTORICO_PUBLICACAO_PATH = 'Home_app/hitorico-publicacao.html'
TEMPLATE_HISTORICO_PATH = 'Home_app/historicos.html'
class HomeTemplateView(TemplateView):
    template_name = "Home_app/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["produtos"] = Produto.objects.all().order_by('-data_de_publicacao')#lista de produtos masi recentes
        #talvez trocar o a chave para produtos_recentes
        context["produtos_mais_votados"] = Produto.objects.all().order_by('ratings')
        
        return context
    

class ShopTemplateView(TemplateView):
    template_name = "Home_app/shop.html"

class DetailTemplateView(TemplateView):
    template_name = "Home_app/detail.html"

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
        context["prateleira"] = Produto.objects.filter(publicado_por=usuario.perfil)[0:5]
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
                rating=0,
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


def populate(request):
    categorias = ["Tecnologia","Remedios","Moveis","Eletrodomesticos","Construção"]
    for categoria in categorias:
        Categoria.objects.create(categoria=categoria,slug=categoria)
    return HttpResponseRedirect(reverse("Home_app:Home"))

