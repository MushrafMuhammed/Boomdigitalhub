from . import views
from django.urls import path

app_name = 'admin'

urlpatterns = [
    path('login',views.loginfun, name='login'),
    path('dashboard',views.dashboardfun, name='dashboard'),  
    path('staff-list',views.staff_fun, name='staff'),  
    path('staff-registration',views.staffRegfun, name='staff-reg'), 
    path('customers-list',views.customerfun, name='customer'),   
    path('stock-details',views.stockfun, name='stock'),   
    path('notFound',views.notFoundfun, name='notFound'),   
]