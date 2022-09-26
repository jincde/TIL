"""practice_0926 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from practices import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('is_odd_even/<int:number>', views.is_odd_even),
    path('crud/<int:num1>/<int:num2>', views.crud),
    path('prelife_input/', views.prelife_input),
    path('prelife_result/', views.prelife_result),
    path('lorem_input/', views.lorem_input),
    path('lorem_result/', views.lorem_result),
]