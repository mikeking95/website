from django.contrib.auth import get_user_model
from django.db import models
from model_bakery import bakery

class Product(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(help_text='in cents',)
    image = models.URLField()
    description = models.TextField()
    category = models.SlugField(max_length=50)
    subcategory = models.CharField(max_length=50)
    keywords = models.CharField(max_length=200)
    url = models.URLField()
    def __str__(self) -> str:
        return self.sku
    
    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.pk])

class Cart(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE
    )
    products = models.ManyToManyField(Product)
