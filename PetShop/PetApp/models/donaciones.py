from django.db import models

class Donacion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, default='Sin descripción')
    cantidad = models.IntegerField(default=0)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='fundaciones/')
