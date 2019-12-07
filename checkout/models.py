from django.db import models

# Create your models here.

class Charge(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        

class Transaction(models.Model):
    
    status_options = [
        ('Pending', "Pending"),
        ('Approved', "Approved"),
        ('Rejected', "Rejected"),
        ('Shipping', "Shipping"),
        ('Delivered', "Delivered"),
        ('Lost', "Lost")
    ]
    
    charge = models.ForeignKey('Charge', on_delete=models.CASCADE, null=True)
    status = models.CharField(blank=False, choices=status_options, max_length=50)
    date = models.DateField()
    cost = models.IntegerField(blank=False)
    
    # if user with transactions has his account deleted, all his transactions will be set to NULL)
    owner = models.ForeignKey("accounts.MyUser", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return "Transaction ID: " + str(self.id) + " | " + "Owner: " + str(self.owner) + " | " + "Cost: " + str(self.cost) + " | " +  "Date: " + str(self.date) + " | " + "Status: " + str(self.status)

class LineItem(models.Model):
    # If product is deleted, information will not go missing
    product = models.ForeignKey('shop.product', null=True, on_delete=models.CASCADE)
    sku = models.CharField(max_length=255, blank=False)
    name = models.CharField(max_length=255, blank=False)
    cost = models.IntegerField(blank=False)
    # define quantity of product bought
    transaction_quantity = models.IntegerField(blank=False, default=0)
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.transaction) + " | " + self.product.name + " : " + self.sku + " | " + "Qty: " + str(self.transaction_quantity)


