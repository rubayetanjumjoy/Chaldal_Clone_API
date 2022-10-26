from django.db import models
from User.models import User
from inventory.models import Product



class orderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)

    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)

    quantity=models.PositiveIntegerField()
    def __str__(self):
        return f"{self.user.name}"
