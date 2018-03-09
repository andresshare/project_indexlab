from django.conf.urls import url
from trabajos.views import trabajos

urlpatterns = [
    url(r'^$', trabajos),
]



