from django.db import models
from django.urls import reverse



class Client(models.Model):
    fname       = models.CharField(max_length=200, null=True, blank=True)
    lname       = models.CharField(max_length=200, null=True, blank=True)
    phone       = models.CharField(max_length=200, null=True, blank=True)
    email       = models.EmailField(max_length=200, null=True, blank=True)
    business    = models.CharField(max_length=200, null=True, blank=True)
    street      = models.CharField(max_length=200, null=True, blank=True)
    city        = models.CharField(max_length=200, null=True, blank=True)
    state       = models.CharField(max_length=200, null=True, blank=True)
    zip_code    = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.business
    

class Group(models.Model):
    name        = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    


class Invoice(models.Model):
    group       = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)   
    client      = models.ForeignKey(Client, max_length=200, null=True, blank=True, on_delete=models.CASCADE)
    date        = models.DateField(auto_now_add=False, null=True, blank=True)
    inv_numb    = models.CharField(max_length=200, null=True, blank=True)
    location    = models.CharField(max_length=200, null=True, blank=True)
    event       = models.CharField(max_length=200, null=True, blank=True)
    amount      = models.CharField(max_length=200, null=True, blank=True)
    status      = models.CharField(max_length=200, null=True, blank=True)  

    def get_absolute_url(self):
        return reverse('product:invoice', kwargs={'pk' == self.pk})

    def __str__(self):
        return str(self.inv_numb) 
    
    

   
class Product(models.Model):
    invoice     = models.ForeignKey(Invoice, null=True, blank=True, on_delete=models.CASCADE)
    name        = models.CharField(max_length=200, null=True, blank=True)
    price       = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    

