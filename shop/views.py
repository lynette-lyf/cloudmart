from django.shortcuts import render
from .models import Product

# Create your views here.
def catalog(request):
    all_products = Product.objects.all()
    # japan_products = Product.objects.filter(origin='Japan')
    return render(request, 'shop/catalog.template.html',{
        'all_products': all_products
        # 'japan_products': japan_products
    })
    
# View individual product
def productview(request, product_id):
    selected_product = Product.objects.get(pk=product_id)
    return render(request, 'shop/product_view.template.html', {
        'selected_product': selected_product
    })

