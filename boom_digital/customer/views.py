from django.http import JsonResponse
from django.shortcuts import redirect, render
from boom_digital import settings

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

from django.http import JsonResponse

def mobileBrandfun(request):
    if request.method == 'POST':
        brand_name = request.POST.get('brand')
        print(brand_name)
        
        if brand_name:
            brandItem = Product.objects.filter(brand__name=brand_name)
            brand_data = list(brandItem.values())

            # Assuming the 'image' field contains the filename, add the full image URL
            for item in brand_data:
                item['image'] = f"{settings.MEDIA_URL}{item['image']}"

            return JsonResponse({'brandItems': brand_data, 'status_code': 200})
        else:
            return JsonResponse({'error': 'Brand name not provided.', 'status_code': 400})
    else:
        return JsonResponse({'error': 'Invalid request method.', 'status_code': 404})

# def mobileBrandfun(request):
#     if request.method == 'POST':
#         print(request.brand)
#         brand_name = request.POST.get('brand')
#         brandItem = Product.objects.filter(
#             category__name = brand_name
#         )
#         # print(brandItem)
       
#         return JsonResponse({'brandItems': brandItem,'status_code':200})
#     else:
#         return JsonResponse({'error': 'Invalid request method.','status_code':404})
    

def laptopfun(request):
    
    return render(request, 'customer/laptop.html')

def desktopfun(request):
    
    return render(request, 'customer/desktop.html')

def tabletfun(request):
    
    return render(request, 'customer/tablets.html')

def accessoriesfun(request):
    
    return render(request, 'customer/accessories.html')