from django.shortcuts import redirect, render

from staff.models import Product

# Create your views here.

def homefun(request):
    productList = Product.objects.all()
    laptop_list = Product.objects.filter(category__name='Laptop')
    laptop_list = Product.objects.filter(category__name='Laptop')
    desktop_list = Product.objects.filter(category__name='Desktop')
    return render(request, 'customer/home.html',{'products':productList,'laptops':laptop_list,'desktops':desktop_list})

def offers_hoverfun(request):
    
    return render(request, 'customer/offers_hover.html')

def offersfun(request):
    
    return render(request, 'customer/offers.html')

def mobilesfun(request):
    mobileList = Product.objects.filter(
        category__name = 'Mobiles'
    )
    
    return render(request, 'customer/mobiles.html',{'mobiles':mobileList})

def laptopfun(request):
    
    return render(request, 'customer/laptop.html')

def desktopfun(request):
    
    return render(request, 'customer/desktop.html')

def tabletfun(request):
    
    return render(request, 'customer/tablets.html')

def accessoriesfun(request):
    
    return render(request, 'customer/accessories.html')