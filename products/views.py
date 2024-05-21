from django.shortcuts import render
from .models import Product

# Create your views here.
def shop_all(request):
    """ Show all products together with sorting order and search selection """

    products = Product.objects.all()

    context = {
        'products': products
    }
    
    return render (request, 'products/products.html', context)
