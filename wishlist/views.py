from django.shortcuts import render, redirect, reverse
from .models import Wishlist
from shop.models import Product

# Create your views here.
    
def view_wishlist(request):
    # request.user = user that is currently logged in
    all_wishlist_items = Wishlist.objects.filter(owner=request.user)
    # total_cost = calculate total cost in wishlist
    
    
    return render(request, 'wishlist/view_wishlist.template.html', {
        'all_wishlist_items': all_wishlist_items
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
        # increases its quantity
        existing_wishlist_item.quantity += 0
        existing_wishlist_item.save()
    return redirect(reverse('view_wishlist'))

def remove_from_wishlist(request, wishlist_id):
    existing_wishlist_item = Wishlist.objects.get(pk=wishlist_id)
    existing_wishlist_item.delete()
    # BEST TO ROUTE IT TO USER'S PREVIOUS PAGE
    return redirect(reverse('view_wishlist'))