from django.shortcuts import redirect, render

# Create your views here.

def homefun(request):
    
    return render(request, 'common/home.html')

# def null_search_redirect(request):
#     return redirect(homefun)

def loginfun(request):
    msg = ""
    # if request.method == "POST":
    #     username = request.POST["email"]
    #     password = request.POST["password"]
    #     try:
    #         customer = Customer.objects.get(email=username, password=password)
    #         request.session["customer_sessionId"] = customer.id
    #         return redirect("common:home")
    #     except:
    #         msg = "invalid password or username"
    return render(request, "common/login.html", {"error_message": msg})

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