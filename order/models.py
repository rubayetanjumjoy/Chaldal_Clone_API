from django.db import models
from User.models import User
from inventory.models import Product
from User.models import Address


class orderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)

    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    address=models.ForeignKey(Address,on_delete=models.CASCADE,blank=True,null=True)
    quantity=models.PositiveIntegerField()
    shipment_id=models.CharField(max_length=15,blank=True,null=True)
    total_price=models.CharField(max_length=200,blank=True,null=True)
    delivery_date=models.CharField(max_length=200,blank=True,null=True)
    timeslot=models.CharField(max_length=200,blank=True,null=True)


    def __str__(self):
        return f"{self.user.name}"
