from . import views
from django.urls import path

app_name = 'admin'

urlpatterns = [
    path('login',views.loginfun, name='login'),
    path('dashboard',views.dashboardfun, name='dashboard'),   
    path('newCategory',views.newCategoryfun, name='newCategory'),   
    path('categories',views.categoryfun, name='category'),
    path('delCategory/<int:Category_id>',views.delCategoryfun, name='delCategory'),
    path('viewCategory/<int:Category_id>',views.viewCategoryfun, name='viewCategory'),
    path('category_exist', views.category_existfun, name='category_exist'), 
    path('brand_exist', views.brand_existfun, name='brand_exist'),   
    path('newBrand',views.newBrandfun, name='newBrand'),   
    path('brands',views.brandfun, name='brand'),
    path('delBrand/<int:brand_id>',views.delbrandfun, name='delBrand'),
    path('viewBrand/<int:brand_id>',views.viewBrandfun, name='viewBrand'),
    path('stock-details',views.stockfun, name='stock'),   
    path('newEmployee',views.newEmployeefun, name='newEmployee'), 
    path('email_exist', views.email_existfun, name='email_exist'),
    path('number_exist', views.number_existfun, name='number_exist'), 
    path('employee-list',views.employee_fun, name='employeeList'),
    path('delEmployee/<int:employee_id>',views.delEmployeefun, name='delEmployee'),
    path('employeeDetails/<int:employee_id>',views.employeeDetailsfun, name='employeeDetails'),
    path('customers-list',views.customerfun, name='customer'),   
    path('stock-details',views.stockfun, name='stock'),  
    path('delProduct/<int:product_id>',views.delProductfun, name='delProduct'), 
    path('addOffer/<int:product_id>',views.addOfferfun, name='addOffer'), 
    path('logout',views.logoutfun, name='logout'),
    path('notFound',views.notFoundfun, name='notFound'),   
]