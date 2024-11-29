from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['ProductID', 'ProductCode', 'ProductName', 'ProductImage', 'CreatedUser', 'IsFavourite', 
                  'Active', 'HSNCode', 'TotalStock', 'name', 'description', 'price', 'stock']

