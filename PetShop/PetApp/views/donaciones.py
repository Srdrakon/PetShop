from django.shortcuts import render
from PetApp.models import Donacion

def donaciones_view(request):
    donaciones = Donacion.objects.all()
    return render(request, 'donaciones.html', {'donaciones': donaciones})
