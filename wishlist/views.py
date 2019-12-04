from django.shortcuts import render, redirect, reverse
from .models import Wishlist
from shop.models import Product
from django.contrib import messages
from django.utils.html import format_html

# Create your views here.

# Calculate wishlist cost to show and hide 'Empty wishlist' container
def calculate_wishlist_cost(request):
    all_wishlist_items = Wishlist.objects.filter(owner=request.user)
    amount = 0
    for wishlist_item in all_wishlist_items:
        amount += wishlist_item.product.cost * wishlist_item.quantity
    
    return amount
    
def view_wishlist(request):
    # request.user = user that is currently logged in
    all_wishlist_items = Wishlist.objects.filter(owner=request.user)
    # total_cost = calculate total cost in wishlist
    total_cost = calculate_wishlist_cost(request)
    
    return render(request, 'wishlist/view_wishlist.template.html', {
        'all_wishlist_items': all_wishlist_items,
        'total_cost':total_cost
    })
    

def add_to_wishlist(request, product_id):
    
    # determine which product the user has added to wishlist
    product = Product.objects.get(pk=product_id)
    
    # if the product already exists in the user's wishlist
    existing_wishlist_item = Wishlist.objects.filter(owner=request.user, product=product).first()
    
    # if the wishlist item does not exist, create a new one
    if existing_wishlist_item == None:
        new_wishlist_item = Wishlist()
        new_wishlist_item.product = product
        new_wishlist_item.owner = request.user
        new_wishlist_item.quantity = 1
        new_wishlist_item.save()
    else:
        # if wishlist item exist, no changes will be made and item will remain in wishlist
        existing_wishlist_item.save()
    
    message = format_html('Product has been <span style="color:#28a745;">added</span> to your <a style="color: #311b92; text-decoration: underline;" href="{}">wishlist</a>.', reverse('view_wishlist'))
    messages.success(request, message)
    return redirect(reverse('catalog'))

def remove_from_wishlist(request, product_id):
    wish_product = Product.objects.get(pk=product_id)
    existing_wishlist_item = Wishlist.objects.get(product=wish_product)
    existing_wishlist_item.delete()
    message = format_html('Product has been <span style="color:#b53737;">removed</span> from your <a style="color: #311b92; text-decoration: underline;" href="{}">wishlist</a>.', reverse('view_wishlist'))
    messages.success(request, message)
    return redirect(reverse('catalog'))


