from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """Add a quantity of the product chosen by the customer to the shopping cart."""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})
    item_id = str(item_id)  # always use string keys

    size = request.POST.get('product_size', None)

    if size:
        # Initialize size structure if needed
        if item_id not in cart:
            cart[item_id] = {'items_by_size': {}}

        current_quantity = cart[item_id]['items_by_size'].get(size, 0)
        new_quantity = current_quantity + quantity

        if new_quantity > product.stock:
            messages.error(
                request,
                f"Sorry, you already have {current_quantity} of size {size.upper()} in your cart. Only {product.stock} available."
            )
            return redirect(redirect_url)

        cart[item_id]['items_by_size'][size] = new_quantity
        if current_quantity > 0:
            messages.success(
                request,
                f"Updated size {size.upper()} {product.name} quantity to {new_quantity}"
            )
        else:
            messages.success(
                request,
                f"Added size {size.upper()} {product.name} to your cart"
            )

    else:
        # Non-size products
        current_quantity = cart.get(item_id, 0)
        new_quantity = current_quantity + quantity

        if new_quantity > product.stock:
            messages.error(
                request,
                f"Sorry, you already have {current_quantity} in your cart. Only {product.stock} available."
            )
            return redirect(redirect_url)

        cart[item_id] = new_quantity
        if current_quantity > 0:
            messages.success(
                request,
                f"Updated {product.name} quantity to {new_quantity}"
            )
        else:
            messages.success(
                request,
                f"Added {product.name} to your cart"
            )

    request.session['cart'] = cart
    return redirect(redirect_url)

def update_cart(request, item_id):
    """ updates quantity of the product chosen by the customer to the shopping cart"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    # STOCK VALIDATION
    if quantity > product.stock:
        messages.error(request, f"Sorry, only {product.stock} of {product.name} available.")
        return redirect(reverse('view_cart'))

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {cart[item_id]["items_by_size"][size]}')
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop[item_id]
                messages.success(request, f'Removed size {size.upper()} {product.name} from your cart')

    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {product.name}  quantity to {cart[item_id]}')
        else:
            cart.pop[item_id]
            messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def remove_from_cart(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your cart')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: (e)')
        return HttpResponse(status=500)

