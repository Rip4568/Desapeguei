from django.urls import include, path

app_name = 'Home_app'

from . import views

urlpatterns = [
    path('',views.HomeTemplateView.as_view(),name='Home'),
    path('shop/',views.ShopTemplateView.as_view(),name='Shop'),
    path('detalhe-do-produto/<slug:id_produto>/',views.DetailTemplateView.as_view(),name='Detail'),
    path('contact/',views.ContactTemplteView.as_view(),name='Contact'),
    path('checkout/',views.CheckoutTemplateView.as_view(),name='Checkout'),
    path('cart/',views.CartTemplateView.as_view(),name='Cart'),
    path('vender-produto/',views.VenderProdutoView.as_view(),name='vender_produto'),
    path('perfil/publicacoes-historico/',views.HistoricoPublicacaoCompletoListView.as_view(),name='historico_publicacao'),
    path('perfil/historicos/',views.HistoricosListView.as_view(),name='historicos'),
    path('populate',views.populate,),
    #LEMBRETE tirar a rota daqui e por no aplicativo Perfil_app.urls
    
]