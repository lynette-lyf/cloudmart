from django.urls import path
from .views import view_wishlist

urlpatterns = [
    path('view_wishlist', view_wishlist, name='view_wishlist')
]