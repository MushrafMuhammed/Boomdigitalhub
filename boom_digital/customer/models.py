from datetime import date, timezone
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

class DeliveryAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=1000)
    place = models.CharField(max_length=100)
    pincode = models.IntegerField()
    email = models.EmailField()
    
    class Meta:
        db_table = 'delivery_address'

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    order_id = models.CharField(max_length = 25, unique = True)
    order_no = models.CharField(max_length = 40)
    total_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    payment_status = models.BooleanField(default = False)
    created_at = models.DateField(default = date.today)
    payment_id = models.CharField(max_length = 100, unique = True, null = True)
    signature_id = models.CharField(max_length = 100, unique = True, null = True)
    order_status = models.CharField(max_length = 100, null = True)
    shipping_address = models.ForeignKey(DeliveryAddress, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'order_tb'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)

    class Meta:
        db_table = 'orderItem_tb'


