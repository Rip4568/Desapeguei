from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView, ListView

from Produtos_app.forms import ProdutoManualForm
from Produtos_app.models import Categoria, Produto
from Historico_app.models import Historico
class HomeTemplateView(TemplateView):
    template_name = "Home_app/index.html"

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
        #context["form"] = ProdutoModelForm # não sera utulizado, o manual é melhor
        usuario = self.request.user
        context["formmanual"] = ProdutoManualForm
        context["usuario"] = usuario
        context["prateleira"] = Produto.objects.filter(publicado_por=usuario.perfil)[0:5]
        return context
    
    def post(self):
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
    TEMPLATE_HISTORICO_PUBLICACAO_PATH = 'Home_app/hitorico-publicacao.html'
    template_name = TEMPLATE_HISTORICO_PUBLICACAO_PATH
    paginate_by = 10
    model = Produto
    context_object_name = 'historico_publicacao'
    
class HistoricosListView(ListView):
    TEMPLATE_HISTORICO_PATH = 'Home_app/historicos.html'
    template_name = TEMPLATE_HISTORICO_PATH
    paginate_by = 10
    model = Historico
    context_object_name = 'historicos'
    


def populate(request):
    categorias = ["Tecnologia","Remedios","Moveis","Eletrodomesticos","Construção"]
    for categoria in categorias:
        Categoria.objects.create(categoria=categoria,slug=categoria)
    return HttpResponseRedirect(reverse("Home_app:Home"))

