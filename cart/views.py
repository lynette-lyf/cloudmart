from django.shortcuts import render, redirect, reverse
from .models import CartItem
from shop.models import Product

# Create your views here.


# Calculate total cost of a single product
#(())
    
# Calculate total cost of cart
def calculate_cart_cost(request):
    all_cart_items = CartItem.objects.filter(owner=request.user)
    amount = 0
    for cart_item in all_cart_items:
        amount += cart_item.product.cost * cart_item.quantity
    
    return amount

    
def view_cart(request):
    # request.user = user that is currently logged in
    all_cart_items = CartItem.objects.filter(owner=request.user)
    # total_cost = calculate total cost in cart
    total_cost = calculate_cart_cost(request)
    # product_cost = calculate total cost of a single product
    #(())
    
    
    return render(request, 'cart/view_cart.template.html', {
        'all_cart_items': all_cart_items,
       #(())
        'total_cost': total_cost/100
    })

    
def add_to_cart(request, product_id):
    
    # determine which product we are buying
    product = Product.objects.get(pk=product_id)
    
    # if the product already exists in the user's shopping cart
    existing_cart_item = CartItem.objects.filter(owner=request.user, product=product).first()
    
    # if the cart item does not exist, create a new one
    if existing_cart_item == None:
        new_cart_item = CartItem()
        new_cart_item.product = product
        new_cart_item.owner = request.user
        new_cart_item.quantity = 1
        new_cart_item.save()
    else:
        # increases its quantity
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    return redirect(reverse('catalog'))
    
def remove_from_cart(request, cart_item_id):
 
    existing_cart_item = CartItem.objects.get(pk=cart_item_id)
    existing_cart_item.delete()
    return redirect(reverse('view_cart'))

def add_one_cart(request, cart_item_id):
    existing_cart_item = CartItem.objects.get(pk=cart_item_id)
    existing_cart_item.quantity += 1
    existing_cart_item.save()
    return redirect(reverse('view_cart'))

def minus_one_cart(request, cart_item_id):
    existing_cart_item = CartItem.objects.get(pk=cart_item_id)
    existing_cart_item.quantity -= 1
    existing_cart_item.save()
    return redirect(reverse('view_cart'))


