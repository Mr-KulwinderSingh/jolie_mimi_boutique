from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProducAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'selling_price',
        'discounted_price',
        'rating',
        'description',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Product, ProducAdmin)

admin.site.register(Category, CategoryAdmin)
