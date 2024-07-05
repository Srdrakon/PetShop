from django.shortcuts import render

def nosotros_view(request):
    return render(request, 'nosotros.html')
