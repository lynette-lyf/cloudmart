from django.shortcuts import render
from .models import Product, Origin
from wishlist.models import Wishlist

# Create your views here.

def catalog(request):
    # View all products
    products = Product.objects.all()
    # Pass in wishlist products to the catalog
    wished_products = Wishlist.objects.filter(owner=request.user)
    return render(request, 'shop/catalog.template.html',{
        'products': products,
        'wished_products': wished_products
    })

# Filter product view by Origin
def catalog_japan(request):
    origin_search = Origin.objects.get(name='Japan')
    products = Product.objects.filter(origin=origin_search)
    return render(request, 'shop/catalog.template.html',{
        'products': products,
    })
    
def catalog_korea(request):
    origin_search = Origin.objects.get(name='Korea')
    products = Product.objects.filter(origin=origin_search)
    return render(request, 'shop/catalog.template.html',{
        'products': products,
    })
    
def catalog_taiwan(request):
    origin_search = Origin.objects.get(name='Taiwan')
    products = Product.objects.filter(origin=origin_search)
    return render(request, 'shop/catalog.template.html',{
        'products': products,
    })
    
# View individual product page
def productview(request, product_id):
    selected_product = Product.objects.get(pk=product_id)
    return render(request, 'shop/product_view.template.html', {
        'selected_product': selected_product
    })

def toggleWishlist (request, product_id):
    wished_items = Wishlist.objects.filter(owner=request.user)
    all_products = Product.objects.all()
    return render(request, 'shop/catalog.template.html', {
        'wished_items': wished_items,
        'all_products': all_products
    })