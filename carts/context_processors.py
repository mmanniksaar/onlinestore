from carts.models import Cart, CartItem
from carts.views import _cart_id


# count total cart items; included in settings.py TEMPLATES section (now its available for all templates)
def counter(request):

    cart_count = 0

    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count +=  cart_item.quantity
        except Cart.DoestNotExist:
            cart_count = 0

    return dict(cart_count=cart_count)
