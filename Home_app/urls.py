from django.urls import path,include

app_name = 'Home_app'

from . import views

urlpatterns = [
    path('',views.HomeTemplateView.as_view(),name='Home'),
    path('shop/',views.ShopTemplateView.as_view(),name='Shop'),
    path('detail/',views.DetailTemplateView.as_view(),name='Detail'),
    path('contact/',views.ContactTemplteView.as_view(),name='Contact'),
    path('checkout/',views.CheckoutTemplateView.as_view(),name='Checkout'),
    path('cart/',views.CartTemplateView.as_view(),name='Cart'),
]