from django.http import JsonResponse
from django.shortcuts import redirect, render

from administrator.models import Admin_users, Brand, Category, Employee

# Create your views here. 

def loginfun(request) :
    msg = ''
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        try :
            admin = Admin_users.objects.get(
                 username = username,
                 password = password
            )
            request.session['admin_sessionID'] = admin.id
            return redirect('admin:dashboard')
        except :
            msg = 'invalid username or password !'

    return render(request, 'administrator/login.html', {'errorMessage' : msg })

def dashboardfun(request):

    return render(request, 'administrator/dashboard.html')
   
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
        msg = "Done"
    return render(request, 'administrator/categoryReg.html',{'successMessage':msg})

def categoryfun(request):
    categories = Category.objects.all()
    count = categories.count()
    return render(request, 'administrator/categories.html',{'categories':categories, 'category_count':count})

def delCategoryfun(request,Category_id):
    delItem = Category.objects.get(
        id = Category_id,
    )
    delItem.delete()
    return redirect('admin:category')

def viewCategoryfun(request,Category_id):
    editItem = Category.objects.get(
        id = Category_id,
    )
    return render(request, 'administrator/viewCategory.html',{'item':editItem})

def editCategoryfun(request):
    msg = ""
    category = Category.objects.get(id=request.POST['request_id'])

    if request.method == 'POST':
        category.name = request.POST['name']
        category.description = request.POST['description']

        if 'logo' in request.FILES:
            category.logo =  request.FILES['logo']

        category.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

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
        msg = "Done"
    return render(request, 'administrator/brandReg.html',{'categories':categories, 'successMessage':msg})

def brandfun(request):
    brands = Brand.objects.all()
    count = brands.count()
    return render(request, 'administrator/brands.html',{'brands':brands, 'brand_count':count})

def delbrandfun(request,brand_id):
    delItem = Brand.objects.get(
        id = brand_id,
    )
    delItem.delete()
    return redirect('admin:brand')

def viewBrandfun(request,brand_id):
    editItem = Brand.objects.get(
        id = brand_id,
    )
    categories = Category.objects.exclude(
        id = editItem.category_id
    )#for exclude the default brand's category
    return render(request, 'administrator/viewBrand.html',{'item':editItem, 'categories':categories})

def editBrandfun(request):

    if request.method == 'POST':
        brand = Brand.objects.get(id=request.POST['request_id'])
        brand.name = request.POST['name']
        brand.description = request.POST['description']
        brand.category = request.POST['category']


        if 'logo' in request.FILES:
            brand.logo = request.FILES['logo']

        brand.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def staffRegfun(request):
    msg = ""
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        employee_email = request.POST['email']
        employee_number = request.POST['number']
        employee_gender = request.POST['gender']
        employee_position = request.POST['position']
        hired_date = request.POST['hired_date']
        employee_qualification = request.POST['qualification']
        employee_profile = request.FILES['profile_img']

        newEmoloyee = Employee (
            first_name = first_name,
            second_name = last_name,
            email = employee_email,
            phone = employee_number,
            gender = employee_gender,
            position = employee_position,
            hired_date = hired_date,
            qualification = employee_qualification,
            profile_img = employee_profile,
        )
        newEmoloyee.save()
        msg = "Done" 
    return render(request, 'administrator/staffReg.html',{'successMessage':msg})


def staff_fun(request):
    employees = Employee.objects.all()
    count = employees.count()
    return render(request, 'administrator/staff.html',{'employees':employees, 'employee_count':count})

def customerfun(request):
    return render(request, 'administrator/customerList.html')

def stockfun(request):
    return render(request, 'administrator/stockDetails.html')

def notFoundfun(request):
    return render(request, 'administrator/notFound.html')