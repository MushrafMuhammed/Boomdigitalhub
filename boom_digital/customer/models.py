from django.db import models
from administrator.models import Customer

from staff.models import Product
# Create your models here.

class Cart(models.Model) :
    product_details = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer =models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'cart'
