from django.urls import path, include
from .views import catalog, productview, catalog_japan, catalog_korea, catalog_taiwan


urlpatterns = [
    path('', catalog, name='catalog'),
    path('products/<product_id>', productview, name='productview'),
    path('japan', catalog_japan, name='catalog_japan'),
    path('korea', catalog_korea, name='catalog_korea'),
    path('taiwan', catalog_taiwan, name='catalog_taiwan')
]