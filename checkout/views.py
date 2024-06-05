from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def  checkout(request):
    cart = request.session.get('cart', {})
    
    if not cart:
        messages.error(request, "There is nothing in the cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html' 
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OL4m2LdZm4Sj6hUXqkQ3Vx5V82CGQanfQFYBCoXFTnszOCcuZTpBjle75SfL8kaIrgRvAT60OaghddXvhtLyY5c001fT4z5h7',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)

