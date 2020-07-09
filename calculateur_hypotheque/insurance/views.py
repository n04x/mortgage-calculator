from django.shortcuts import render

def insuranceView(request):
    return render(request, 'insurance.html')

# Create your views here.
def insuranceCalculator(request):
    house_price = float(request.POST['houseprice'])
    # cash_down = float(request.POST['cashdown'])
    # mortgage = house_price - cash_down
    # x = cash_down / house_price
    result = []

    result.append(0.04 * (house_price - (house_price * 0.05))) 
    result.append(0.031 * (house_price - (house_price * 0.10)))
    result.append(0.028 * (house_price - (house_price * 0.15)))
    result.append(0.024 * (house_price - (house_price * 0.20)))
    result.append(0)

    # result = "{:,.2f}$".format(result)
    context = {
        'result' : result
    }

    return render(request, 'insurance.html', context)