from django.shortcuts import redirect, render

# Create your views here.

def homefun(request):
    
    return render(request, 'common/home.html')

# def null_search_redirect(request):
#     return redirect(homefun)


def offers_hoverfun(request):
    
    return render(request, 'common/offers_hover.html')

def offersfun(request):
    
    return render(request, 'common/offers.html')

def mobilesfun(request):
    
    return render(request, 'common/mobiles.html')

def laptopfun(request):
    
    return render(request, 'common/laptop.html')

def desktopfun(request):
    
    return render(request, 'common/desktop.html')

def tabletfun(request):
    
    return render(request, 'common/tablets.html')

def accessoriesfun(request):
    
    return render(request, 'common/accessories.html')