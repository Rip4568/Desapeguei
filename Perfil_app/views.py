from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class PerfilTemplateView(TemplateView):
    template_name = "Home_app/perfil.html"