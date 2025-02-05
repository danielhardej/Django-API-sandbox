# myapp/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Item

class ItemModelTest(TestCase):
    def setUp(self):
        Item.objects.create(name="Test Item", description="Test Description")

    def test_item_creation(self):
        item = Item.objects.get(name="Test Item")
        self.assertEqual(item.description, "Test Description")

class ItemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item = Item.objects.create(name="Test Item", description="Test Description")

    def test_get_item(self):
        response = self.client.get(reverse('item-detail', kwargs={'pk': self.item.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Item")