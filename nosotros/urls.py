from django.conf.urls import url, include
from nosotros.views import nosotros

urlpatterns = [
    url(r'^$', nosotros, name='nosotros'),
]
