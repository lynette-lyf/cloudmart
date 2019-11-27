from django.urls import path, include
from .views import catalog, productview


urlpatterns = [
    path('', catalog, name='catalog'),
    path('products/<product_id>', productview, name='productview')
]