from django.contrib import admin

# Register your models here.

from .models import Perfil

""" @admin.register()
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['usuario','nome','ingressou'] """
    
admin.site.register(Perfil)