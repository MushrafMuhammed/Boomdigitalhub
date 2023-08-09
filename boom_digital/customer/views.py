from decimal import Decimal
from django.urls import reverse
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render
from administrator.models import Brand, Category, Customer
from boom_digital import settings
from django.http import JsonResponse
from customer.models import Cart
from django.db.models import Sum


from staff.models import Product

# Create your views here.

def newCustomerfun(request):
    msg = ""
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            customer = Customer(
                name = name,
                phone = phone,
                email = email,
                password = password,
            )
            customer.save()
            return redirect("customer:login")
        except:
            msg = "invalid entry"
    return render(request, "customer/newCustomer.html", {"error_message": msg})

def loginfun(request):
    msg = ""
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        try:
            customer = Customer.objects.get(email=username, password=password)
            request.session["customer_sessionId"] = customer.id
            return redirect("customer:home")
        except:
            msg = "invalid password or username"
    return render(request, "customer/login.html", {"error_message": msg})

def homefun(request):
    productList = Product.objects.all()
    laptop_list = Product.objects.filter(category__name='Laptops')
    desktop_list = Product.objects.filter(category__name='Desktops')
    mobile_list = Product.objects.filter(category__name='Mobiles')
    tablet_list = Product.objects.filter(category__name='Tablets')
    accessories_list = Product.objects.filter(category__name='Accessories')
    return render(request, 'customer/home.html',{'products':productList,'laptops':laptop_list,'desktops':desktop_list,'accessories':accessories_list,'mobiles':mobile_list,'tablets':tablet_list})

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

def productDetailsfun(request,product_id):
    print(product_id)
    product = Product.objects.get(
        id = product_id
    )
    return render(request, 'customer/product_details.html',{'product':product})

def cartItemsfun(request):
    cartProducts = Cart.objects.filter(customer=request.session.get("customer_sessionId"))
    cartCount = cartProducts.count()
    grandTotal = cartProducts.aggregate(total_price=Sum("sub_total")).get(
        "total_price", 0
    )  # aggregation functions Sum()

    if grandTotal is None:
        grandTotal = 0.00

    return render(request,"customer/cartItems.html",
        {"cartProducts": cartProducts, "cartCount": cartCount, "grandTotal": grandTotal})

def cartfun(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, "customer/product_not_found.html")
    product = Product.objects.get(id=product_id)
    if "customer_sessionId" in request.session:
        product_exist = Cart.objects.filter(
            product_details=product_id, 
            customer=request.session["customer_sessionId"]
        ).exists()
        
        # Use the appropriate price based on offer_price availability
        if product.offer_price:
            cart_price = product.offer_price
        else:
            cart_price = product.price

        if not product_exist:
            cart = Cart(
                customer_id=request.session["customer_sessionId"],
                product_details_id=product_id,
                quantity=1,
                sub_total=cart_price,
            )
            cart.save()
            return cartItemsfun(request)

        else:
            request.session["cart_msg"] = "item already in your cart"
            return redirect(reverse("customer:home"))
    else:
        return redirect("customer:login")
    
def delCart(request, cart_id):
    # cart item to be deleted
    del_item = Cart.objects.get(
        id=cart_id, customer=request.session.get("customer_sessionId")
    )
    del_item.delete()
    return redirect("customer:cartItems")

def update_itemTotalfun(request):
    # Get new quantity and product_id from the AJAX POST request
    quantity = request.POST['quantity']
    product_id = request.POST['product_id']
    print(quantity,product_id)
    # Retrieve the product object and its price
    try:
        product = Product.objects.get(id=product_id)
        price = product.price
        # print(product,price)
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found."}, status=404)

    # Calculate the new total price
    try:
        sub_total = int(quantity) * price
        # print(total)
    except ValueError:
        return JsonResponse({"error": "Invalid quantity."}, status=400)

    # Update the Cart with the new price and quantity
    try:
        cart_item = Cart.objects.get(product_details_id=product_id, customer_id=request.session["customer_sessionId"])
        cart_item.quantity = quantity
        cart_item.sub_total = sub_total
        cart_item.save()
    except Cart.DoesNotExist:
        return JsonResponse({"error": "Cart item not found."}, status=404)

    # Return the updated subtotal as JSON response
    return JsonResponse({"subTotal": sub_total})

def checkoutfun(request):
    

        return render(request,'customer/checkout.html')
  

def success_pagefun(request):
    
    return render(request,'customer/success_page.html')

def product_not_foundfun(request):
    
    return render(request,'customer/product_not_found.html')