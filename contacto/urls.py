from django.conf.urls import url, include
from contacto.views import contacto

urlpatterns = [
    url(r'^$', contacto, name='contacto'),
]
