from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import contacto


class ContactoTests(TestCase):
    def test_contacto_view_status_code(self):
        url = reverse('contacto')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


def test_contacto_url_resolves_contacto_view(self):
        view = resolve('/')
        self.assertEquals(view.func, contacto)
