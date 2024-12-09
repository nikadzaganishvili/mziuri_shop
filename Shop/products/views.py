from django.shortcuts import render
from .models import Product

def home(request):
    product = Product.objects.all()
    return render(request, 'home.html', context={'products': product})

def product_detail(request):
    return render(request, 'product_detail.html')


