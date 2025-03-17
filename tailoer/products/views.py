from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/products.html', context)


def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'products/product.html', context)


def createProduct(request):
    profile = request.user.profile
    form = ProductForm()

    if request.method == 'POST':
        print(request.POST)
        form = ProductForm(request.POST, request.user)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = profile
            product.save()
            return redirect('profile', profile)

    context = {'form': form}
    return render(request, 'products/new_product.html', context)


def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')

    context = {'form': form, 'product': product}
    return render(request, 'products/edit_product.html', context)


def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('products')

    context = {'product': product}
    return render(request, 'products/delete_product.html', context)
