import os
import django
import json
from decimal import Decimal

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PetShop.settings')
django.setup()

from PetApp.models import Producto

# Ruta al archivo JSON
json_path = os.path.join(os.path.dirname(__file__), 'static/json/productos.json')

# Cargar los datos del JSON
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extraer los productos de la estructura JSON
productos = data['categories']

# Borrar los productos existentes (opcional)
Producto.objects.all().delete()

# Crear nuevos productos
for producto_data in productos:
    producto_dict = {
        'id_category': producto_data['idCategory'],
        'nombre': producto_data['strCategory'],
        'imagen': producto_data['strCategoryThumb'],
        'descripcion': producto_data['strCategoryDescription'],
        'precio': Decimal(producto_data['precioProducto'].replace('$', '').replace('.', '').replace(',', '.'))
    }
    Producto.objects.create(**producto_dict)

print("Productos cargados correctamente.")
