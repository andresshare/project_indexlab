from django.shortcuts import render
from .models import Contacto
from .forms import ContactoForm


def contacto(request):
    contactos = Contacto.objects.all()

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
    else:
        formulario = ContactoForm()

    return render(request, 'contacto.html', {'contactos': contactos, 'form': formulario})
