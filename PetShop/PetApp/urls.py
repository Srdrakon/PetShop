from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from PetApp.views import index_view, inicio_view, contacto_view, donaciones_view, nosotros_view,tienda_view
from PetApp.views import registro_view,login_view,logout_view
urlpatterns = [
    path('', inicio_view, name='inicio'),
    path('inicio/', inicio_view, name='inicio'),
    path('contacto/', contacto_view, name='contacto'),
    path('donaciones/', donaciones_view, name='donaciones'),
    path('nosotros/', nosotros_view, name='nosotros'),
    path('tienda/', tienda_view, name='tienda'),
    path('registro/', registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
