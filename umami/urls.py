"""umami URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from core import views as core_views
from pasteleria import views as pasteleria_views

urlpatterns = [
    path('',core_views.index, name='index'),
    path('acerca_de/',core_views.acerca_de, name='acerca_de'),
    path('contacto/',core_views.contacto, name='contacto'),
    path('picoteo/',core_views.picoteo, name='picoteo'),
    path('tortas/',pasteleria_views.tortas, name='tortas'),
    path('admin/', admin.site.urls),
    path('dimension/', core_views.dimension, name='dimension'),
]
