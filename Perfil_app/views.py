from django.shortcuts import render
from django.views.generic import TemplateView

from Historico_app.models import Historico


class PerfilTemplateView(TemplateView):
    template_name = "Home_app/perfil.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["compra_e_venda"] = Historico.objects.all()[0:5]
        return context
    