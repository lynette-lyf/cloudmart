from django.urls import path, include
from .views import checkout, charge

urlpatterns = [
    path('charge/', charge, name='charge')
]