from django.urls import path
from .views import view_wishlist, add_to_wishlist, remove_from_wishlist

urlpatterns = [
    path('view_wishlist', view_wishlist, name='view_wishlist'),
    path('add_to_wishlist/<product_id>', add_to_wishlist, name='add_to_wishlist'),
     path('remove_from_wishlist/<wish_list_id>', remove_from_wishlist, name='remove_from_wishlist'),
]