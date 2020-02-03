from .models import Charge
from django import forms

class OrderForm(forms.ModelForm):
    class Meta:
        model = Charge
        fields = (
            'full_name', 'phone_number', 'country', 'postcode',
            'town_or_city', 'street_address1', 'street_address2'
        )

class PaymentForm(forms.Form):

    # use list comprehension to generate the months and years
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2051)]
    credit_card_name = forms.CharField(max_length=50, required=False)
    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)