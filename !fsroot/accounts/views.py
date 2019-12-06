from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm, get_user_model
from cart.views import view_cart_amount
from cart.models import CartItem

# import in the login_required annotation
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    cart_amount = CartItem.objects.filter(owner=request.user).count()
    return render(request, 'accounts/index.template.html', {
        'cart_amount': cart_amount
    })

# Logout function
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))
    
    '''
    Error: Logout redirect to Django Admin logout page instead of main landing page
    '''

# Login function


def login(request):
    """Returns the login page"""
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST) # populate the form from what the user has keyed in
        if login_form.is_valid():
            # attempt to check the username and password is valid
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            messages.success(request, "You have successfully logged in")
            if user:
                # log in the user
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error('None', "Invalid username or password")
    else:
        login_form = UserLoginForm()
        return render(request, 'accounts/login.template.html', {
            'form':login_form
        })
        
    '''
    Error: Login redirect to /accounts page (with incomplete static template) instead of main landing page
    '''

@login_required    
def profile(request):
    User = get_user_model()
    user = User.objects.get(email=request.user.email)
    cart_amount = CartItem.objects.filter(owner=request.user).count()
    return render(request, 'accounts/profile.template.html', {
        'user' : user,
        'cart_amount': cart_amount
    })
    
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #check if the username and password matches
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                #acutally log the user in
                auth.login(user=user, request=request)
                messages.success(request, "You have registered successfully")
            else:
                messages.error(request, "You failed to register")
            return redirect(reverse('index'))
        else:
            return render(request, "accounts/register.template.html", {
                'form': form
            })
    else:
        register_form = UserRegistrationForm()
        return render(request, "accounts/register.template.html", {
            'form': register_form
    })
    
    '''
    Registration and login form to be on the same page render[login.template.html]: how to call 2 diff forms in login.template.html?
    '''