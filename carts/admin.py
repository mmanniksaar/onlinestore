from django.contrib import admin
from django.utils.html import format_html
from store.models import Product

from carts.models import Cart, CartItem

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'add_date')

class CartItemAdmin(admin.ModelAdmin):

    list_display = ('product', 'cart', 'quantity', 'is_active',)

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)