from django.http import JsonResponse
from django.shortcuts import render
from administrator.models import Brand, Category
from boom_digital import settings
from django.http import JsonResponse

from staff.models import Product

# Create your views here.

def homefun(request):
    productList = Product.objects.all()
    laptop_list = Product.objects.filter(category__name='Laptops')
    desktop_list = Product.objects.filter(category__name='Desktop')
    return render(request, 'customer/home.html',{'products':productList,'laptops':laptop_list,'desktops':desktop_list})

def offers_hoverfun(request):
    
    return render(request, 'customer/offers_hover.html')

def offersfun(request):
    # Filter products with non-null offer_price
    offerProducts = Product.objects.filter(offer_price__isnull=False)
    return render(request, 'customer/offers.html', {'offerProducts': offerProducts})

def mobilesfun(request):
    brandList = Brand.objects.filter(
        category__name = 'Mobiles'
    )
    mobileList = Product.objects.filter(
        category__name = 'Mobiles'
    )
    category = Category.objects.get(name = 'Mobiles')
    categoryId = category.id
    return render(request, 'customer/mobiles.html',{'brands':brandList,'mobiles':mobileList,'category_id':categoryId})

def getBrand(request):
    if request.method == 'POST':
        brand_name = request.POST.get('brand')
        categoryId = request.POST.get('categoryId')
        # print(brand_name)
        
        if brand_name:
            brandItem = Product.objects.filter(brand__name=brand_name,category_id = categoryId)
            brand_data = list(brandItem.values())

            # Assuming the 'image' field contains the filename, add the full image URL
            for item in brand_data:
                item['image'] = f"{settings.MEDIA_URL}{item['image']}"

            return JsonResponse({'brandItems': brand_data, 'status_code': 200})
        else:
            return JsonResponse({'error': 'Brand name not provided.', 'status_code': 400})
    else:
        return JsonResponse({'error': 'Invalid request method.', 'status_code': 404})
    

def laptopfun(request):
    brandList = Brand.objects.filter(
        category__name = 'Laptops'
    )
    laptopList = Product.objects.filter(
        category__name = 'Laptops'
    )
    category = Category.objects.get(name='Laptops')
    categoryId = category.id
    return render(request, 'customer/laptop.html', {'brands':brandList,'laptops':laptopList,'category_id':categoryId})

def laptopBrandfun(request):
    if request.method == 'POST':
        brand_name = request.POST.get('brand')
        categoryId = request.POST.get('categoryId')

        
        if brand_name:
            brandItem = Product.objects.filter(brand__name=brand_name,category_id = categoryId)
            brand_data = list(brandItem.values())

            # Assuming the 'image' field contains the filename, add the full image URL
            for item in brand_data:
                item['image'] = f"{settings.MEDIA_URL}{item['image']}"

            return JsonResponse({'brandItems': brand_data, 'status_code': 200})
        else:
            return JsonResponse({'error': 'Brand name not provided.', 'status_code': 400})
    else:
        return JsonResponse({'error': 'Invalid request method.', 'status_code': 404})

def desktopfun(request):
    brandList = Brand.objects.filter(
        category__name = 'Desktops'
    )
    desktopList = Product.objects.filter(
        category__name = 'Desktops'
    )
    category = Category.objects.get(name='Desktops')
    categoryId = category.id
    return render(request, 'customer/desktop.html',{'desktops':desktopList,'brands':brandList,'category_id':categoryId})

def tabletfun(request):
    brandList = Brand.objects.filter(
        category__name = 'Tablets'
    )
    tabletList = Product.objects.filter(
        category__name = 'Tablets'
    )
    category = Category.objects.get(name='Tablets')
    categoryId = category.id
    return render(request, 'customer/tablets.html',{'tablets':tabletList,'brands':brandList,'category_id':categoryId})

def accessoriesfun(request):
    accessories = Product.objects.filter(
        category__name = 'Accessories'
    )
    return render(request, 'customer/accessories.html',{'accessories':accessories})