from django.contrib import admin
from .models import Contacto, Producto, Noticia, Evento, CustomUser

# Register your models here.


##
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
admin.site.register(CustomUser, CustomUserAdmin)
##
admin.site.register(Contacto)
admin.site.register(Producto)
admin.site.register(Noticia)
admin.site.register(Evento)
admin.site.register(CustomUser)

