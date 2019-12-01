from django.shortcuts import render
from .models import Wishlist

# Create your views here.
    
def view_wishlist(request):
    # request.user = user that is currently logged in
    all_wishlist_items = Wishlist.objects.filter(owner=request.user)
    # total_cost = calculate total cost in cart
    
    
    return render(request, 'wishlist/view_wishlist.template.html', {
        'all_wishlist_items': all_wishlist_items
    })