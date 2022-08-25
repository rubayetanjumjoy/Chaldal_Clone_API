from django.db import models
from django.shortcuts import render
# Create your models here.

class Cart(models.Model):
    cart = models.ForeignKey('User.User' ,on_delete=models.CASCADE)
    product=models.CharField(max_length=200)
    quantity = models.EmailField(max_length=20)

    def __str__(self):
        return self.id




