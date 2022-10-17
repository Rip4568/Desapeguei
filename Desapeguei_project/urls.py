from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #rota para o acesso de administração
    path('admin/', admin.site.urls),
    #rota para acessar as configurações de login
    path('accounts/', include('allauth.urls')),
    #rotas dos aplicativos
    path('',include('Home_app.urls')),
    path('perfil/',include('Perfil_app.urls')),
    #3rd party rotas
    path('ratings/', include('star_ratings.urls', namespace='ratings')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
