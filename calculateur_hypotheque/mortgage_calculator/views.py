from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import CityTaxes

import numpy as np
import requests
from bs4 import BeautifulSoup

# Create your views here.
def mortgageView(request):
    all_cities_taxes = CityTaxes.objects.order_by('city_name')
    # all_cities_taxes = CityTaxes.objects.all()
    context={
        'all_cities': all_cities_taxes
    }
    return render(request, 'cities_taxes.html', context)

def calculatorView(request):
    return render(request, 'calculator.html')

def calculateMortgage(request):
    house_price = request.POST['houseprice']
    cash_down = request.POST['cashdown']
    mortgage_rate = request.POST['rate']
    mortgage_rate = float(mortgage_rate)/100
    mortgage_rate_periodic = (mortgage_rate/2+1)**(1/6) - 1
    mortgage_payment_period = 25*12                         # Based on 25 years.
    mortgage_loan = float(house_price) - float(cash_down)
    # monthly = house_price
    monthly = -1*np.pmt(mortgage_rate_periodic, mortgage_payment_period, mortgage_loan)
    monthly = "{:,.2f}$".format(monthly)
    context = {
        'monthly' : monthly
    }
    return render(request, 'calculator.html', context)

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects.
    all_cities = CityTaxes.objects.order_by('city_name')
    context = {
        'all_cities' : all_cities
    }

    return render(request, 'index.html', context)

def searchCity(request):
    city = request.POST['city']
    all_cities = CityTaxes.objects.all()
    for c in all_cities:
        if city == c.city_name:
            result = c
            break
    
    context = {
        'result' : result
    }

    return render(request, 'search.html', context)

def taxesView(request):
    return render(request, 'taxes_calc.html')
    
def taxesCalculation(request):
    property_value = request.POST['value']
    city = request.POST['city']
    all_cities = CityTaxes.objects.all()
    for c in all_cities:
        if city == c.city_name:
            result = c
            break

    if result != None:
        rate = result.city_taxe
        cost = float(property_value)/100 * float(rate)
    
    context = {
        'city_name' : result.city_name,
        'city_taxe' : result.city_taxe,
        'cost' : cost
    }

    return render(request, 'taxes_calc.html', context)

