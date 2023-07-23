from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('login', views.loginfun, name='login'),
    path('dashboard',views.dashboardfun, name='dashboard'),  
    path('profile', views.profilefun, name='profile'),
    path('add-product', views.addproductsfun, name='addProducts'),
    path('productDetails', views.productDetailsfun, name='productDetails'),
    path('orders', views.orderfun, name='order'),
    path('stockDetails', views.stockDetailsfun, name='stockDetails'),
    path('logout', views.logoutfun, name='logout'),

]
