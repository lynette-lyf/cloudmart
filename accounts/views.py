from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm, get_user_model

from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import redirect

# import in the login_required annotation
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'accounts/index.template.html')

# Logout function
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    # return redirect(reverse('index'))
    return redirect('%s?userAction=%s' % (settings.LOGOUT_URL, request.path))

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
                return redirect('%s?userAction=%s' % (settings.LOGIN_URL, request.path))
            else:
                login_form.add_error('None', "Invalid username or password")
    else:
        login_form = UserLoginForm()
        return render(request, 'accounts/login.template.html', {
            'form':login_form
        })

@login_required    
def profile(request):
    User = get_user_model()
    user = User.objects.get(email=request.user.email)
    return render(request, 'accounts/profile.template.html', {
        'user' : user
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
