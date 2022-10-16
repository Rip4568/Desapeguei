from .models import Perfil
from django.contrib import admin

""" @admin.register()
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['usuario','nome','ingressou'] """
    
admin.site.register(Perfil)