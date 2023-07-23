
from django.shortcuts import redirect, render

# from staff.models import Product, Seller

# Create your views here.

def loginfun(request):
    
    return render(request, "staff/login.html")

def logoutfun(request):

    return redirect('staff:login')

def dashboardfun(request):
    return render(request, 'staff/dashboard.html')

def profilefun(request):

    return render(request, 'staff/profile.html')

def addproductsfun(request):

    return render(request, 'staff/addProduct.html')

def productDetailsfun(request):

    return render(request, 'staff/productDetails.html')

def orderfun(request):

    return render(request, 'staff/orders.html')

def stockDetailsfun(request):

    return render(request, 'staff/stockDetails.html')





