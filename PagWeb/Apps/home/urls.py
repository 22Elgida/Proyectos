"""PagWeb URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from Apps.home.views import HomeView, EstudianteView, AdminView, AcercaView

app_name='home'
urlpatterns = [
    path('', HomeView.as_view(), name='homeapp'),
    path('estudiante/', EstudianteView.as_view(), name='estudianteapp'),
    path('admin/', AdminView.as_view(), name='adminapp'),
    path('acerca/', AcercaView.as_view(), name='acercapp')

]
