"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from hello.views import myView
from todo.views import todoView, addTodo
from mortgage_calculator.views import mortgageView, calculatorView, calculateMortgage, index, searchCity, taxesCalculation, taxesView
from insurance.views import insuranceView, insuranceCalculator

urlpatterns = [
    path('index/', index, name='index'),
    path('admin/', admin.site.urls),
    path('sayHello/', myView),
    path('todo/', todoView, name='todo'),
    path('addTodo/', addTodo),
    path('cities_taxes/', mortgageView, name='cities_taxes'),
    path('calculator/', calculatorView, name='calculator'),
    path('calculate/', calculateMortgage),
    path('search/', searchCity),
    path('taxes_calc/', taxesView, name='taxes_calc'),
    path('tax_calculate/', taxesCalculation),
    path('insurance/', insuranceView),
    path('calculateInsurance/', insuranceCalculator),
]
