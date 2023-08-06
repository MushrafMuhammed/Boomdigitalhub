from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = 'customer'

urlpatterns = [
    # path('', views.null_search_redirect),
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

]