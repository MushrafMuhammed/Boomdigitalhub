from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = 'customer'

urlpatterns = [
    # path('', views.null_search_redirect),
    path('customer_registration', views.newCustomerfun, name='newCustomer'),
    path('login', views.loginfun, name='login'),
    path('home', views.homefun, name='home'),
    path('offers', views.offersfun, name='offers'),
    path('offers_hover', views.offers_hoverfun, name='offers_hover'),
    path('mobiles', views.mobilesfun, name='mobile'),
    path('getBrand', views.getBrand, name='getBrand'),
    path('laptops', views.laptopfun, name='laptop'),
    path('laptopBrand', views.laptopBrandfun, name='laptopBrand'),
    path('desktops', views.desktopfun, name='desktop'),
    path('tablets', views.tabletfun, name='tablet'),
    path('accessories', views.accessoriesfun, name='accessories'),
    path('productDetails/<int:product_id>',views.productDetailsfun, name='productDetails'),
    path('cartItems', views.cartItemsfun, name='cartItems'),
    path('cart/<int:product_id>', views.cartfun, name='cart'),
    path('delCart/<int:cart_id>', views.delCart, name='delCart'),
    path('update_itemTotal', views.update_itemTotalfun, name='update_itemTotal'),
    path('addressDetails', views.address_detailsfun, name='address-details'),
    path('checkout', views.checkoutfun, name='checkout'),
    path('order_product', views.order_productfun, name='order_product'),
    path('callback/<int:a_id>', views.callbackfun, name='callback'),
    path('success_page', views.success_pagefun, name='success_page'),
    path('product_not_found', views.product_not_foundfun, name='product_not_found'),

]