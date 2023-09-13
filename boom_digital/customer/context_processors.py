from django.shortcuts import render
from administrator.models import Customer
from customer.models import Cart


def customer_name(request):
    customer_id = request.session.get("customer_sessionId")
    if customer_id is not None:
        customer = Customer.objects.get(id=customer_id)
        cartItems = Cart.objects.filter(customer = customer_id)
        cartCount = cartItems.count() 
        return {'customer_name': customer.name, 'cartCount':cartCount}
    else:
        return {'customer_name': None}  # default value if no customer is found

