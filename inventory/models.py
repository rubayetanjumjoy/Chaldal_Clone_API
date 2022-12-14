from django.db import models
# Create your models here.

class Product(models.Model):
    catagory=models.ForeignKey('Catagory', on_delete=models.CASCADE)
    title= models.CharField(max_length=200,null=False,blank=False)
    description = models.CharField(max_length=200,blank=True)
    image=models.ImageField()
    price = models.IntegerField()
    def __str__(self):
        return self.title

class Catagory(models.Model):
    name= models.CharField(max_length=200,null=False,blank=False)
    slug = models.SlugField(max_length=40)
    icon=models.CharField(max_length=600,blank=True)
    



    def __str__(self):
        return self.name




