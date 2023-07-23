from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = 'common'

urlpatterns = [
    # path('', views.null_search_redirect),
    path('home', views.homefun, name='home'),
    path('login', views.loginfun, name='login' ),
    path('offers', views.offersfun, name='offers' ),
    path('offers_hover', views.offers_hoverfun, name='offers_hover' ),
    path('mobiles', views.mobilesfun, name='mobile' ),
    path('laptops', views.laptopfun, name='laptop' ),
    path('desktops', views.desktopfun, name='desktop' ),
    path('tablets', views.tabletfun, name='tablet' ),
    path('accessories', views.accessoriesfun, name='accessories' ),
    





]