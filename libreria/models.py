from django.db import models


# TODO: 1FA - 2FA
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    autor = models.CharField(max_length=200)
    publicacion = models.DateField()
