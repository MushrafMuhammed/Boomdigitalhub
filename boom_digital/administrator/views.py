from django.shortcuts import redirect, render

# Create your views here.

def loginfun(request) :
    msg = ''
    if request.method == 'POST' :
        username = request.POST['email']
        password = request.POST['password']

        try :
            admin = admin.objects.get(
                 username = username,
                 password = password
            )
            request.session['admin_sessionID'] = admin.id
            return redirect('admin:home')
        except :
            msg = 'invalid username or password !'

    return render(request, 'administrator/login.html', {'errorMessage' : msg })

def dashboardfun(request):
    return render(request, 'administrator/dashboard.html')

def staff_fun(request):
    return render(request, 'administrator/staff.html')

def staffRegfun(request):
    return render(request, 'administrator/staffReg.html')

def customerfun(request):
    return render(request, 'administrator/customerList.html')

def stockfun(request):
    return render(request, 'administrator/stockDetails.html')

def notFoundfun(request):
    return render(request, 'administrator/notFound.html')