from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    path('login', views.loginfun, name='login'),
    path('dashboard',views.dashboardfun, name='dashboard'),  
    path('profile', views.profilefun, name='profile'),
    path('newProduct', views.newProductfun, name='newProduct'),
    path('product_exist', views.product_existfun, name='product_exist'), 
    path('categoryItem', views.categoryItemfun, name='categoryItem'),
    path('productList', views.productListfun, name='productList'),
    path('delProduct/<int:product_id>',views.delProductfun, name='delProduct'),
    path('productDetails/<int:product_id>',views.productDetailsfun, name='productDetails'),
    path('orders', views.orderfun, name='order'),
    path('stockDetails', views.stockDetailsfun, name='stockDetails'),
    path('logout', views.logoutfun, name='logout'),

]
