from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


def trabajos(request):
    return render(request, 'trabajo.html')
