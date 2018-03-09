from django.conf.urls import url
from nosotros.views import nosotros

urlpatterns = [
    url(r'^$', nosotros),
]
