from django.shortcuts import render

def contacto_view(request):
    return render(request, 'contacto.html')
