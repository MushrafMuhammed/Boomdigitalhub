from django.db import models

from administrator.models import Brand, Category

# Create your models here.

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    current_stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images/')
    offer_price = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'product'


