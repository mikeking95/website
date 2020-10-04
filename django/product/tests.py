from django.test import TestCase
from product.models import Product
from django.contrib.auth.models import User
from model_bakery import baker
import pprint

class TestProductModels(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        print('db test')
        testuser = User.objects.create_user(
            username='testuser', password='12345')
        testuser2 = User.objects.create_user(
            username="evil_user", password='123456')
        cls.new = Product.objects.create(
            sku="TEST-001-A", name="Test Product Alpha", price=1234)
    
    def test_get_absolute_url(self):
        self.new.sku = Product.objects.get(id=1)
    

class TestNew(TestCase):
    def setUp(self):
        self.product = baker.make('product.Product')
        pprint(self.product.__dict__)
    def test_model_str(self):
        sku = Product.objects.create(sku="TESTY-01")
        
        self.assertEqual(str(sku), "TESTY-01")

