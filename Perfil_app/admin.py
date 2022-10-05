from .models import Perfil,Historico
from django.contrib import admin

""" @admin.register()
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['usuario','nome','ingressou'] """
    
admin.site.register(Perfil)
admin.site.register(Historico)