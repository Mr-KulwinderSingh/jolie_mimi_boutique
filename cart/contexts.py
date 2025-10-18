from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):
    cart_items = []
    total = Decimal('0.00')
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        try:
            product = get_object_or_404(Product, pk=item_id)
            if isinstance(item_data, int):
                # Single item without size
                total += Decimal(item_data) * product.selling_price
                product_count += item_data
                cart_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'product': product
                })
            elif isinstance(item_data, dict):
                # Item with sizes
                items_by_size = item_data.get('items_by_size', {})
                for size, quantity in items_by_size.items():
                    total += Decimal(quantity) * product.selling_price
                    product_count += quantity
                    cart_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'size': size, 
                    })
        except Product.DoesNotExist:
            # Handle the case where the product does not exist
            pass

    if total < Decimal(settings.FREE_DELIVERY_THRESHOLD):
        delivery = total * (Decimal(settings.STANDARD_DELIVERY_PERCENTAGE) / 100)
        free_delivery_delta = Decimal(settings.FREE_DELIVERY_THRESHOLD) - total
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
