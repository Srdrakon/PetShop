from django.db import models

class Producto(models.Model):
    id_category = models.CharField(max_length=50, default='sin_categoria')
    nombre = models.CharField(max_length=200)
    imagen = models.URLField(default='https://example.com/default_image.jpg')
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nombre
