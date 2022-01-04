from django.contrib import admin
from .models import Product
from django.utils.html import format_html


# Register your models here.

class ProductAdmin(admin.ModelAdmin):

    def product_image_tag(self, obj):
        return format_html('<img src="{}" width="90" height="90" />'.format(obj.product_image.url) )

    list_display = ('product_name', 'slug', 'price', 'stock', 'category', 'modified_date', 'is_available', 'product_image_tag',)
    prepopulated_fields = {'slug': ('product_name',)}
    product_image_tag.short_description = 'Product image'


admin.site.register(Product, ProductAdmin)