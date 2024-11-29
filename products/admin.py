from django.contrib import admin

# Register your models here.
from .models import Products, Variant, SubVariant

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('ProductID', 'ProductCode', 'ProductName', 'CreatedDate', 'Active')
    search_fields = ('ProductCode', 'ProductName')
    list_filter = ('Active', 'IsFavourite')
    ordering = ('-CreatedDate',)

@admin.register(Variant)
class VariantsAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'options')  # 'options' needs to be callable
    search_fields = ('name',)
    list_filter = ('product',)
    
@admin.register(SubVariant)
class SubVariantsAdmin(admin.ModelAdmin):
    list_display = ('variant', 'name', 'stock')
    search_fields = ('name',)
    list_filter = ('variant',)


