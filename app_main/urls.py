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
    path('lista_usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('perfil/', views.perfil, name='perfil'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('condiciones/', views.condiciones, name='condiciones'),
    path('privacidad/', views.privacidad, name='privacidad'),
    path('buscar_por_categoria/<int:categoria_id>/', views.buscar_por_categoria, name='buscar_por_categoria'),
]
