import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PetShop.settings')
django.setup()

from PetApp.models import Donacion

json_path = os.path.join(os.path.dirname(__file__), 'static/json/organizaciones.json')

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

organizaciones = data['fundaciones']

Donacion.objects.all().delete()

for organizacion_data in organizaciones:
    organizacion_dict = {
        'nombre': organizacion_data['nombreFundacion'],
        'descripcion': organizacion_data['descripcionFundacion'],
        'cantidad': 0,
        'fecha': '2023-01-01',
        'imagen': 'fundaciones/' + organizacion_data['imagenFundacion']
    }
    Donacion.objects.create(**organizacion_dict)

print("Organizaciones cargadas correctamente.")
