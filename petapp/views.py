from django.shortcuts import render

# Create your views here.

from .models import Noticia, Evento
######

####


#################
def vista_index(request):
    noticias = Noticia.objects.all()  # Obtener todas las noticias
    eventos = Evento.objects.all()    # Obtener todos los eventos

    return render(request, 'petapp/index.html', {'noticias': noticias, 'eventos': eventos})

def vista_nosotros(request):
    return render(request, 'petapp/nosotros.html')

def vista_tienda(request):
    return render(request, 'petapp/tienda.html')

def vista_donaciones(request):
    return render(request, 'petapp/donaciones.html')    

def vista_contacto(request):
    return render(request, 'petapp/contacto.html')

def detalle_noticia(request, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)
    return render(request, 'petapp/detalle_noticia.html', {'noticia': noticia})

def detalle_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    return render(request, 'petapp/detalle_evento.html', {'evento': evento})
