from django.test import TestCase
from restaurant.models import Menu
from decimal import Decimal

# Write Test Case for Menu Model

class MenuTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(title="Test Menu", price=Decimal('10.00'), inventory=10)

    def test_menu_price(self):
        menu = Menu.objects.get(title="Test Menu")
        self.assertEqual(menu.price, Decimal('10.00'))

    def test_menu_inventory(self):
        menu = Menu.objects.get(title="Test Menu")
        self.assertEqual(menu.inventory, 10)
    
    def test_menu_title(self):
        menu = Menu.objects.get(title="Test Menu")
        self.assertEqual(menu.title, "Test Menu")
    
    def test_menu_str(self):
        menu = Menu.objects.get(title="Test Menu")
        self.assertEqual(str(menu), "Test Menu : 10.00")

