from django.shortcuts import render
from administrator.models import Customer


def customer_name(request):
    customer_id = request.session.get("customer_sessionId")
    if customer_id is not None:
        customer = Customer.objects.get(id=customer_id)
        return {'customer_name': customer.name}
    else:
        return {'customer_name': None}  # default value if no customer is found

