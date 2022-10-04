from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

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


