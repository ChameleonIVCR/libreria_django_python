from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse

from .models import Libro


def Index(request):
    libros = Libro.objects.all()
    return render(request, 'index.html', {'libros': libros})


def API(request, id_libro=None):
    if id_libro:
        respuesta = model_to_dict(
            Libro.objects.get(pk=id_libro)
        )
    else:
        respuesta = list(Libro.objects.values())

    return JsonResponse(respuesta, safe=False)
