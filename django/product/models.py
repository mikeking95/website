from django.contrib.auth import get_user_model
from django.db import models
from model_bakery import baker


class Image(models.Model):
    shop = models.CharField(max_length=100, blank=True)
    url = models.URLField()
    name = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text='99.99')
    description = models.TextField()
    category = models.SlugField(max_length=50)
    subcategory = models.CharField(max_length=50)
    keywords = models.CharField(max_length=200)
    images = models.ManyToManyField(Image)

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
