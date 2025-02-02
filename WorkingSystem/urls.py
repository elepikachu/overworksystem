"""WorkingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),
    path('update', views.update_view),
    path('info', views.info_view),
    path('food', views.food_view),
    path('project/', include('project.urls')),
    path('checal/', include('checal.urls')),
    path('buyitem/', include('buyitem.urls')),
    path('fuelcell/', include('fuelcell.urls')),
    path('robots.txt', views.robots_txt),
]
