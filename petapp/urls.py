from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.vista_index, name='index'),
    path('nosotros/', views.vista_nosotros, name='nosotros'),
    path('tienda/', views.vista_tienda, name='tienda'),
    path('donaciones/', views.vista_donaciones, name='donaciones'),
    path('contacto/', views.vista_contacto, name='contacto'),
    path('noticia/<int:noticia_id>/', views.detalle_noticia, name='detalle_noticia'),
    path('evento/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),



]
