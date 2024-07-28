"""
URL configuration for chaiAurDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views   # . is called current directory
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'HOME'),   # '' is home route (not like 'home/'), name para is optional
    path('about/', views.about),
    path('contact/', views.contact),
    # For App 'chai' with is listed in setting.py under 'APPS' : ['chai'] 
    path("chai/", include('chai.urls')),   # Control of all urls of app 'chai' goes to urls.py of app 'chai'

    path("__reload__/", include("django_browser_reload.urls"))  # For Auto Reloading, NOTE: Keep this in last line only
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
