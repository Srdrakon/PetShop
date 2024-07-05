# PETSHOP_DJANGO

```
PetShop/
├── PetShop/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── PetApp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   └── donaciones.py
│   ├── views/
│   │   ├── __init__.py
│   │   ├── inicio.py
│   │   ├── index.py
│   │   ├── contacto.py
│   │   ├── donaciones.py
│   │   ├── nosotros.py
│   │   ├── login.py
│   │   ├── registro.py
│   │   └── logout.py
│   ├── urls.py
│   ├── services/
│   │   └── __init__.py
│   ├── form.py
│
├── templates/
│   ├── contacto.html
│   ├── donaciones.html
│   ├── index.html
│   ├── inicio.html
│   ├── nosotros.html
│   └── tienda.html
│   └── login.html
│   └── registro.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── json/
│       ├── organizaciones.json
│       └── productos.json
│
├── media/
│   ├── fundaciones/
│   │   ├── callejeros_de_la_calle.png
│   │   ├── chile_mestizos.png
│   │   ├── fundacion_adopta.png
│   │   └── siete_vidas.png
│   ├── contacto.png
│   ├── donaciones.png
│   ├── nosotros.png
│   └── tienda.png
│
├── manage.py
├── requirements.txt
├── load_donaciones.py
└── load_productos.py
```

## Instalación

Instrucciones para configurar el proyecto localmente.

1. Clona el repositorio:
   ```bash
   https://github.com/Hoxton87/PETSHOP_DJANGO.git
  

2. Navega al directorio del proyecto.
3. Activar entorno virtual.
   ```bash
   env\Scripts\activate
4. migraciones.
   ```bash
   python manage.py migrate
6. Cargar Datos de Donaciones y Productos
   ```bash
   python load_donaciones.py
   python load_productos.py

5. Corremos el Server.
   ```bash
   python manage.py runserver
