from django.conf.urls import url, include
from trabajos.views import trabajos

urlpatterns = [
    url(r'^$', trabajos, name="trabajos"),
]
