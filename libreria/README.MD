# libreria_django_python

Implementación basica de Django Python; cuenta con un modelo básico "Libro", una vista en tabla para mostrar los datos "Index", y una vista "API" para consultar datos del modelo, ya sea completamente, o por id, en formato JSON.

## Instalación

Requiere Python >= 3.6, preferiblemente 64 bits.

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Para añadir datos al modelo, el panel de administración se encuentra en ```http://127.0.0.1:8000/admin/```

## Comportamiento

La aplicación corre el servicio en el puerto 8000, usando como index a la vista "Index", que lista la información presente en la base de datos en una tabla. También ofrece la vista API, donde, si se llama sin argumentos, o ruta, devolvera toda la información presente en la base de datos en un objeto JSON.

En caso de estar presenten un número como ruta, consultara a éste en la base de datos, y retornara el modelo encontrado.

## Dependencias

- Python >= 3.6
- Django 3.2.7

![alt-text](https://i.ibb.co/1Th4fPX/Capture.png)