from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

from restaurant.models import *
from restaurant.views import *

# Create your tests here.
class MenuViewTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345') # used to instantiate password with hashing
        user.save()

        Menu.objects.create(title="Apple", price=2, inventory=100)
        Menu.objects.create(title="Banana", price=4, inventory=75)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/') # put / BEFORE AND AFTER URL !!! (or use django.urls reverse)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.login(username="testuser", password="12345")
        self.assertEqual(response, True)

    def test_template_used(self):
        print(reverse("index"))
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "index.html")
        