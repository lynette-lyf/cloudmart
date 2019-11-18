from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

# our own user model
from .models import MyUser

class UserLoginForm(forms.Form):
    """Form to login user"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# User Registration Form
class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)
    
    def clean_email(self):
        User = get_user_model()
        
        user_provided_email = self.cleaned_data.get('email')
        
        # check if the email already exists inside the User table
        if User.objects.filter(email=user_provided_email):
            # if so, raise an error, registration process will be stopped
            raise forms.ValidationError("This email address is already in use")
        
        return user_provided_email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise ValidationError("Please provide your password twice")
        
        if password1 != password2:
            raise ValidationError("Passwords must match")
        
        #return password2 as it is because it passes all the validation rules
        return password2
        
    class Meta:
        model = MyUser
        fields = ['email', 'username', 'password1', 'password2']