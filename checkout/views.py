from django.shortcuts import render, HttpResponse
from .forms import OrderForm, PaymentForm
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from cart.models import CartItem
from .models import Charge, Transaction, LineItem

import stripe

def calculate_cart_cost(request):
    all_cart_items = CartItem.objects.filter(owner=request.user)
    amount = 0
    for cart_item in all_cart_items:
        amount += cart_item.product.cost * cart_item.quantity
    
    return amount

# Create your views here.
def checkout(request):
    amount = calculate_cart_cost(request)
    return render(request, 'checkout/charge.template.html', {
        'amount': amount/100
    })

def charge(request):
    amount = calculate_cart_cost(request)
    
    if request.method == 'GET':
        
        # create a new transaction
        transaction = Transaction()
        transaction.owner = request.user
        transaction.cart_items = CartItem.objects.filter(owner=request.user)
        transaction.status = "pending"
        transaction.date = timezone.now()
        transaction.save()
        
        all_cart_items = CartItem.objects.filter(owner=request.user)
        for cart_item in all_cart_items:
            lineItem = LineItem()
            lineItem.transaction = transaction
            lineItem.product = cart_item.product
            lineItem.name = cart_item.product.name
            lineItem.sku = cart_item.product.sku
            lineItem.cost = cart_item.product.cost
            lineItem.save()
        
        order_form = OrderForm()
        payment_form = PaymentForm()
        return render(request, 'checkout/charge.template.html', {
                'order_form' : order_form,
                'payment_form': payment_form,
                'amount': amount,
                'transaction': transaction,
                'publishable': settings.STRIPE_PUBLISHABLE_KEY
            })
    else:
        
        transaction_id = request.POST['transaction_id']
        transaction = Transaction.objects.get(pk=transaction_id)
        # only approve the transaction when status is 'Pending'
        if transaction.status != 'pending':
            return HttpResponse("Transaction has expired.")
                
        # processing the payment
        stripeToken = request.POST['stripe_id']
        
        # set the secret key for the STRIPE API
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount= int(request.POST['amount']),
                    currency='usd',
                    description='Payment',
                    card=stripeToken
                )
                
                if customer.paid:
                    
                    order = order_form.save(commit=False)
                    order.date=timezone.now()
                    order.save()
                    
                    # update the transaction status
                    transaction.status = 'approved'
                    transaction.charge = order
                    transaction.save()
                    
                    # update the stock
                    line_items = LineItem.objects.filter(transaction_id=transaction_id)
                    for each_line_item in line_items:
                        each_line_item.product.quantity -= 1
                        each_line_item.product.save()
                    
                    # remove cart items
                    cart_items = CartItem.objects.filter(owner=request.user).delete()
    
                        
                    
                    return render(request, 'checkout/thankyou.template.html')
                else:
                    messages.error(request, "Your card has been declined")
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
        else:
            return render(request, 'checkout/charge.template.html', {
            'order_form' : order_form,
            'payment_form': payment_form,
            'amount': amount,
            'publishable': settings.STRIPE_PUBLISHABLE_KEY
        })