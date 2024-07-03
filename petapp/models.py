from django.db import models
######
from django.contrib.auth.models import AbstractUser

# Create your models here.
#########








#########
class Donacion(models.Model):
    nombre = models.CharField(max_length=64)
    email = models.EmailField(max_length=120)
    cantidad = models.FloatField()

    def __str__(self):
        return self.nombre
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    direccion = models.CharField(max_length=255)
    acepto_terminos = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return self.nombre
