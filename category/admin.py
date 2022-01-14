from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):

    def category_image_tag(self, obj):
        return format_html('<img src="{}" width="90" height="90" />'.format(obj.category_image.url) )

    list_display = ('category_name', 'description', 'slug', 'category_image_tag',)#
    prepopulated_fields = {'slug': ('category_name',)}
    category_image_tag.short_description = 'Category image'


admin.site.register(Category, CategoryAdmin)
