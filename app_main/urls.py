from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('acerca_nosotros/', views.acerca_nosotros, name='acerca_nosotros'),
    path('pagina_registro/', views.pagina_registro, name='pagina_registro'),
    path('registrar/emprendedor/', views.registrar, name='registrar'),
    path('registrar/consumidor/', views.registrar_consumidor, name='registrar_consumidor'),
    path('iniciar_sesion', views.inicar_sesion, name='iniciar_sesion'),
    path('perfil/', views.perfil, name='perfil'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
