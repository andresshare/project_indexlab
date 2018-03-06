from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Contacto


def contacto(request):
    contactos = Contacto.objects.all()
    return render(request, 'Contacto.html', {'contactos': contactos})



