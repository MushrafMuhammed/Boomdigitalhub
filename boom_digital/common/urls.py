from django.urls import path
from django.shortcuts import redirect
from . import views
app_name = 'common'

urlpatterns = [
    path('', views.null_search_redirect),
    path('home', views.homefun, name='home'),
    path('login', views.loginfun, name='login' ),
]