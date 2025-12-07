from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def electronics(request):
    elec_products = {
        "Product1": "Mac",
        "Product2": "iPhone",
        "Product3": "Dell"
    }
    return render(request, 'templatesApp/ShoppingApp/product.html', context=elec_products)

def toys(request):
    toy_products = {
        "Product1": "Remote Car",
        "Product2": "Helicopter",
        "Product3": "Gun"
    }
    return render(request, 'templatesApp/ShoppingApp/product.html', context=toy_products)

def shoes(request):
    shoe_products = {
        "Product1": "Nike",
        "Product2": "Adidas",
        "Product3": "Eco"
    }
    return render(request, 'templatesApp/ShoppingApp/product.html', context=shoe_products)

def index(request):
    return render(request, 'templatesApp/ShoppingApp/index.html')