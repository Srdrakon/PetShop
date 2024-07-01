from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect##
from .models import Noticia, Evento
######
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
####


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    
    form = CustomUserCreationForm()
    return render(request, 'petapp/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirige a la página principal después del login
    else:
        form = CustomAuthenticationForm()
    return render(request, 'petapp/login.html', {'form': form})



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
