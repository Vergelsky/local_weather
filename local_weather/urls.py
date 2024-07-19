"""
URL configuration for config project.

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
from django.urls import path

from local_weather.apps import LocalWeatherConfig
from local_weather.views import index, get_weather, cities_report

app_name = LocalWeatherConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('get-weather/', get_weather, name='get-weather'),
    path('cities-report/', cities_report, name='cities-report'),

]
