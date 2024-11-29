from django.shortcuts import render, redirect, get_object_or_404
from .models import Products
from django.contrib import messages
from .forms import ProductForm

# Product list (for the frontend, not API)
def product_list(request):
    products = Products.objects.prefetch_related('variants__subvariant_set').all()
    return render(request, 'products/product_list.html', {'products': products})

# Add product (for the frontend, not API)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

# Edit product (for the frontend, not API)
def edit_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)  
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form})

# Delete product (for the frontend, not API)
def delete_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

# Product detail (for the frontend, not API)
def product_detail(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})






