"""
URL configuration for boom_digital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from common.views import homefun
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homefun , name='common_home'),
    path('admin/', include('administrator.urls')),
    path('common/', include('common.urls')),
    path('staff/', include('staff.urls')),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)