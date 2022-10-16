from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.

from django.views.generic import TemplateView

from Produtos_app.forms import ProdutoManualForm, ProdutoModelForm
from Produtos_app.models import Categoria

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
        context["form"] = ProdutoModelForm
        context["formmanual"] = ProdutoManualForm
        return context
    
def populate(request):
    categorias = ["Tecnologia","Remedios","Moveis","Eletrodomesticos","Construção"]
    for categoria in categorias:
        Categoria.objects.create(categoria=categoria,slug=categoria)
    return HttpResponseRedirect(reverse("Home_app:Home"))

