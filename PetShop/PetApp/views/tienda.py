# PetApp/views/tienda.py
from django.shortcuts import render
from PetApp.models import Producto

def tienda_view(request):
    categoria = request.GET.get('categoria', None)
    if categoria:
        productos = Producto.objects.filter(id_category=categoria)
    else:
        productos = Producto.objects.all()
    
    context = {
        'productos': productos
    }
    return render(request, 'tienda.html', context)
