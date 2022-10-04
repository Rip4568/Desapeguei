from django.urls import path

from . import views

app_name = 'Perfil_app'

urlpatterns = [
    path('',views.PerfilTemplateView.as_view(),name='Perfil')
]