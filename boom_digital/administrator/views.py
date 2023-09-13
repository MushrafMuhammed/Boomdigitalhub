import random
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from administrator.decorators import auth_admin

from administrator.models import Admin_users, Brand, Category, Customer, Employee
from boom_digital import settings
from customer.models import Order
from staff.models import Product

# Create your views here. 

def loginfun(request) :
    msg = ''
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        try :
            admin = Admin_users.objects.get(
                 username = username,
                 password = password
            )
            request.session["admin_sessionID"] = admin.id
            return redirect('admin:dashboard')
        except :
            msg = 'invalid username or password !'

    return render(request, 'administrator/login.html', {'errorMessage' : msg })

@auth_admin
def dashboardfun(request):
    productList = Product.objects.all()
    proCount = productList.count()
    customerList = Customer.objects.all()
    cusCount = customerList.count()
    employees = Employee.objects.all()
    empCount = employees.count()
    orderList= Order.objects.all()
    orderCount = orderList.count()
    return render(request, 'administrator/dashboard.html',{'productCount':proCount,'customerCount':cusCount,'employeeCount':empCount,'orderCount':orderCount})

@auth_admin   
def newCategoryfun(request):
    msg = ""
    if request.method == 'POST':
        category_name = request.POST['name']
        category_des = request.POST['description']
        category_logo = request.FILES['logo']

        newCategory = Category (
            name = category_name,
            description = category_des,
            logo = category_logo,
        )
        newCategory.save()
        msg = "Category added successfully"
    return render(request, 'administrator/categoryReg.html',{'successMessage':msg})

@auth_admin
def category_existfun(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        category_exists = Category.objects.filter(name__iexact=category_name).exists()
        return JsonResponse({'exists': category_exists})

    return JsonResponse({'error': 'Invalid request'})

@auth_admin   
def categoryfun(request):
    categories = Category.objects.all()
    count = categories.count()
    return render(request, 'administrator/categories.html',{'categories':categories, 'category_count':count})

def delCategoryfun(request,Category_id):
    if "admin_sessionID" in request.session:
        delItem = Category.objects.get(
            id = Category_id,
        )
        delItem.delete()
        return redirect('admin:category')
    else:
        return redirect("admin:login")

def viewCategoryfun(request,Category_id):
    if "admin_sessionID" in request.session:
        editItem = Category.objects.get(
            id = Category_id,
        )
        if request.method == "POST":
            editItem.name = request.POST.get('category_name')
            editItem.description = request.POST.get('description')

        if 'logo' in request.FILES:
            editItem.logo = request.FILES.get('logo')
        editItem.save()
        return render(request, 'administrator/viewCategory.html',{'item':editItem})
    else:
        return redirect("admin:login")

@auth_admin   
def newBrandfun(request):
    categories = Category.objects.all()
    msg = ""
    if request.method == 'POST':
        brand_category = request.POST['category']
        brand_name = request.POST['name']
        brand_des = request.POST['description']
        brand_logo = request.FILES['logo']

        newBrand = Brand (
            category_id = brand_category,
            name = brand_name,
            description = brand_des,
            logo = brand_logo,
        )
        newBrand.save()
        msg = "Brand added successfully"
    return render(request, 'administrator/brandReg.html',{'categories':categories, 'successMessage':msg})

@auth_admin
def brand_existfun(request):
    if request.method == 'POST':
        brandName = request.POST.get('brand_name')
        brand_exists = Brand.objects.filter(name__iexact=brandName).exists()
        return JsonResponse({'exists': brand_exists})

    return JsonResponse({'error': 'Invalid request'})

@auth_admin
def brandfun(request):
    brands = Brand.objects.all()
    count = brands.count()
    return render(request, 'administrator/brands.html',{'brands':brands, 'brand_count':count})

def delbrandfun(request,brand_id):
    if "admin_sessionID" in request.session:

        delItem = Brand.objects.get(
            id = brand_id,
        )
        delItem.delete()
        return redirect('admin:brand')
    else:
        return redirect("admin:login")


def viewBrandfun(request,brand_id):
    if "admin_sessionID" in request.session:
        editItem = Brand.objects.get(
            id = brand_id,
        )
        categories = Category.objects.exclude(
            id = editItem.category_id
        )#for exclude the default brand's category

        if request.method == "POST":
            editItem.name = request.POST.get('name')
            editItem.description = request.POST.get('description')

            category_id = request.POST.get('category')
            category_instance = Category.objects.get(id=category_id)
            editItem.category = category_instance


        if 'logo' in request.FILES:
            editItem.logo = request.FILES.get('logo')
        editItem.save()
        return render(request, 'administrator/viewBrand.html',{'item':editItem, 'categories':categories})
    else:
        return redirect("admin:login")

@auth_admin
def newEmployeefun(request):
    msg = ""
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        second_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        gender = request.POST.get('gender')
        position = request.POST.get('position')
        hired_date = request.POST.get('hired_date')
        qualification = request.POST.get('qualification')
        profile_img = request.FILES.get('profile_img')
        # Generate a password
        password = first_name.lower() + '@boom' 
        message = 'Hai Your username is ' + str(email) + 'and temporary password is ' + password
        
        # Create a new user with the generated password
        newEmoloyee = Employee (
            first_name = first_name,
            second_name = second_name,
            email = email,
            password = password,
            phone =phone,
            gender = gender,
            position = position,
            hired_date = hired_date,
            qualification =qualification,
            profile_img = profile_img,
        )

        # Send email   
        send_mail(
            'Your New Account in Boom Digital Hub',
            message,
            settings.EMAIL_HOST_USER,
            [request.POST.get('email')],
            fail_silently = False
        )
        newEmoloyee.save()
        msg = "Registration completed" 
    return render(request, 'administrator/newEmployee.html',{'successMessage':msg})

@auth_admin
def email_existfun(request):
    if request.method == 'POST':
        emailId = request.POST.get('email')
        email_exists = Employee.objects.filter(email__iexact = emailId).exists()
        return JsonResponse({'exists': email_exists})

    return JsonResponse({'error': 'Invalid request'})

@auth_admin
def number_existfun(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        number_exists = Employee.objects.filter(phone = number).exists()
        return JsonResponse({'exists': number_exists})

    return JsonResponse({'error': 'Invalid request'})

def employee_fun(request):
    employees = Employee.objects.all()
    count = employees.count()
    return render(request, 'administrator/employeeList.html',{'employees':employees, 'employee_count':count})

def delEmployeefun(request,employee_id):
    if "admin_sessionID" in request.session:
        delEmployee = Employee.objects.get(
            id = employee_id,
        )
        delEmployee.delete()
        return redirect('admin:employeeList')
    else:
        return redirect("admin:login")


def employeeDetailsfun(request,employee_id):
    if "admin_sessionID" in request.session:
        editemployee = Employee.objects.get(
            id = employee_id,
        )

        if request.method == "POST":
            editemployee.first_name = request.POST.get('first_name')
            editemployee.second_name = request.POST.get('last_name')
            editemployee.email = request.POST.get('email')
            editemployee.phone = request.POST.get('number')
            editemployee.gender = request.POST.get('gender')
            editemployee.position = request.POST.get('position')
            editemployee.qualification = request.POST.get('qualification')
        if 'profile_img' in request.FILES:
            editemployee.profile_img = request.FILES.get('profile_img')    
        editemployee.save()

        return render(request, 'administrator/employeeDetails.html',{'editemployee':editemployee})

    else:
        return redirect("admin:login")
    

@auth_admin
def customerfun(request):
    customerList = Customer.objects.all()
    count = customerList.count()
    return render(request, 'administrator/customerList.html',{'customers':customerList,'customerCount':count})

@auth_admin
def stockfun(request):
    productList = Product.objects.all()
    productCount = productList.count()

    # Calculate total current_stock
    total_current_stock = sum(product.current_stock for product in productList)
    return render(request, 'administrator/stockDetails.html',{'products':productList,'count':productCount, 'total_stock':total_current_stock})

def delProductfun(request,product_id):
    if "admin_sessionID" in request.session:
        delItem = Product.objects.get(
            id = product_id,
        )
        delItem.delete()
        return redirect('admin:stock')
    else:
        return redirect("admin:login")

def addOfferfun(request,product_id):
    if "admin_sessionID" in request.session:
        editproduct = Product.objects.get(
            id = product_id,
        )

        if request.method == "POST":
            editproduct.offer_price = request.POST.get('offer_price')
        editproduct.save()
        return render(request, 'administrator/addOffers.html',{'editproduct':editproduct})
    else:
        return redirect("admin:login")    

def logoutfun(request):
    del request.session["admin_sessionID"]
    request.session.flush()
    return redirect("admin:login")  # Redirect to the common home page after logout

def notFoundfun(request):
    return render(request, 'administrator/notFound.html')