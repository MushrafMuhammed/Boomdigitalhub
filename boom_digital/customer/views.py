from django.shortcuts import redirect, render

# Create your views here.

def homefun(request):
    
    return render(request, 'customer/home.html')

def offers_hoverfun(request):
    
    return render(request, 'customer/offers_hover.html')

def offersfun(request):
    
    return render(request, 'customer/offers.html')

def mobilesfun(request):
    
    return render(request, 'customer/mobiles.html')

def laptopfun(request):
    
    return render(request, 'customer/laptop.html')

def desktopfun(request):
    
    return render(request, 'customer/desktop.html')

def tabletfun(request):
    
    return render(request, 'customer/tablets.html')

def accessoriesfun(request):
    
    return render(request, 'customer/accessories.html')