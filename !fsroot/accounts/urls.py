from django.urls import path, include
from .views import index, logout, login, profile, register

urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('profile/', profile, name='user_profile'),
    path('register/', register, name='user_register'),
    path('register/password_reset', register, name='password_reset')
]