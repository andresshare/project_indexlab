from django.conf.urls import url, include
from home.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
]
