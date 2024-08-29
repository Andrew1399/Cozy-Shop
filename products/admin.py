from django.contrib import admin
from products.models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'available', 'created', 'updated']
    list_editable = ['price', 'available']
    list_filter = ['available', 'created', 'updated']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Product, ProductAdmin)