from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import redirect, render

from administrator.models import Brand, Category, Employee
from customer.models import Order, OrderItem
from staff.decorators import auth_employee
from staff.models import Product
from django.http import JsonResponse

# Create your views here.

def loginfun(request):
    msg = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            employee = Employee.objects.get(
                email=username,
                password=password
            )
            request.session["employee_sessionID"] = employee.id
            return redirect("employee:dashboard")
        except:
            msg = "invalid username or password !"

    return render(request, 'employee/login.html', {"errorMessage": msg})

@auth_employee
def dashboardfun(request):
    productList = Product.objects.all()
    productCount = productList.count()
    orderList= Order.objects.all()
    orderCount = orderList.count()

    # Calculate total current_stock
    total_current_stock = sum(product.current_stock for product in productList)
    return render(request, "employee/dashboard.html",{'count':productCount, 'total_stock':total_current_stock,'orderCount':orderCount})

@auth_employee
def profilefun(request):
    user = Employee.objects.get(
        id = request.session["employee_sessionID"]
    )
    return render(request, "employee/profile.html",{'logged_user':user})

@auth_employee
def newProductfun(request):
    categoryList  = Category.objects.all()
    brandList = Brand.objects.all()
    msg = ''
    if request.method == 'POST':
        category = request.POST['category']
        brand = request.POST['brand']
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        offer_price = request.POST['offer_price']
        current_stock = request.POST['current_stock']
        image = request.FILES['image']

        # Handle empty offer_price
        if not offer_price:
            offer_price = None
        else:
            offer_price = Decimal(offer_price)

        newProduct = Product(
            category_id = category,
            brand_id = brand,
            name = name,
            description = description,
            price = price,
            offer_price = offer_price,
            current_stock = current_stock,
            image = image,
        )
        newProduct.save()
        msg = "New product added"
    return render(request, "employee/newProduct.html",{'categories':categoryList,'brands':brandList,'successMessage':msg})

@auth_employee
def categoryItemfun(request):
    if request.method == 'POST':
        selectedCategory = request.POST.get('category')
        # print(selectedCategory)

        if selectedCategory:
            selectedBrands = Brand.objects.filter(
                category_id=selectedCategory
            ).values()  # Convert QuerySet to a list of dictionaries
            return JsonResponse({'brands': list(selectedBrands), 'status_code': 200})
        else:
            return JsonResponse({'error': 'Brand name not provided.', 'status_code': 400})
    else:
        return JsonResponse({'error': 'Invalid request method.', 'status_code': 404})

@auth_employee
def productListfun(request):
    productList = Product.objects.all()
    totalProduct = productList.count()
    return render(request, "employee/productList.html",{'products':productList,'count':totalProduct})

def delProductfun(request,product_id):
    if "employee_sessionID" in request.session:
        delItem = Product.objects.get(
            id = product_id,
        )
        delItem.delete()
        return redirect('employee:productList')
    else:
        return redirect("employee:login")

def productDetailsfun(request,product_id):
    if "employee_sessionID" in request.session:
        editproduct = Product.objects.get(
            id = product_id,
        )
        categoryList = Category.objects.exclude(
            id = editproduct.category_id
        )
        brandList = Category.objects.exclude(
            id = editproduct.brand_id
        )
        return render(request, 'employee/productDetails.html',{'editemployee':editproduct, 'categories':categoryList, 'brands':brandList})
    else:
        return redirect("employee:login")

@auth_employee
def orderfun(request):
    orderList= Order.objects.all()
    count = orderList.count()
    # Access order and related items
    itemsWithOrders = OrderItem.objects.all().select_related('order')
    return render(request, 'employee/orders.html',{'orderCount':count,'orderItems':itemsWithOrders})

@auth_employee
def stockDetailsfun(request):
    productList = Product.objects.all()
    productCount = productList.count()

    # Calculate total current_stock
    total_current_stock = sum(product.current_stock for product in productList)
    return render(request, 'employee/stockDetails.html',{'products':productList,'count':productCount, 'total_stock':total_current_stock})

def logoutfun(request):
    del request.session["employee_sessionID"]
    request.session.flush()
    return redirect("employee:login")  # Redirect to the common home page after logout