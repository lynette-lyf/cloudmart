from django.urls import path
from .views import add_to_cart, view_cart, remove_from_cart, add_one_cart, minus_one_cart

urlpatterns = [
    path('add_to_cart/<product_id>', add_to_cart, name='add_to_cart'),
    path('view', view_cart, name='view_cart'),
    path('remove_from_cart/<cart_item_id>', remove_from_cart, name='remove_from_cart'),
    path('add_one_cart/<cart_item_id>', add_one_cart, name='add_one_cart'),
    path('minus_one_cart/<cart_item_id>', minus_one_cart, name='minus_one_cart')
]


