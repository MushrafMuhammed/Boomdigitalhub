from decimal import Decimal
from django.shortcuts import redirect, render

from administrator.models import Brand, Category, Employee
from staff.models import Product

# from staff.models import Product, Seller

# Create your views here.


def loginfun(request):
    msg = ""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username,password)

        try:
            emplooyee = Employee.objects.get(email=username, phone=password)
            request.session["emplooyee_sessionID"] = emplooyee.id
            return redirect("employee:dashboard")
        except:
            msg = "invalid username or password !"

    return render(request, 'employee/login.html', {"errorMessage": msg})


def logoutfun(request):
    del request.session["emplooyee_sessionID"]
    return redirect("employee:login")


def dashboardfun(request):
    return render(request, "employee/dashboard.html")


def profilefun(request):
    user = Employee.objects.get(
        id = request.session["emplooyee_sessionID"]
    )
    return render(request, "employee/profile.html",{'logged_user':user})


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


def productListfun(request):
    productList = Product.objects.all()
    totalProduct = productList.count()
    return render(request, "employee/productList.html",{'products':productList,'count':totalProduct})

def delProductfun(request,product_id):
    delItem = Product.objects.get(
        id = product_id,
    )
    delItem.delete()
    return redirect('employee:productList')

def productDetailsfun(request,product_id):
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


def orderfun(request):
    return render(request, "employee/orders.html")


def stockDetailsfun(request):
    productList = Product.objects.all()
    productCount = productList.count()
    # Calculate total current_stock
    total_current_stock = sum(product.current_stock for product in productList)
    return render(request, "employee/stockDetails.html",{'products':productList,'count':productCount, 'total_stock':total_current_stock})
