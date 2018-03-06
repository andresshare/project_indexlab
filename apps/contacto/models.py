from django.db import models


class Contacto(models.Model):

    nombre = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    telefono = models.CharField(max_length=15)
    mensaje = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre
