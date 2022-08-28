from .models import Product
from .models import Catagory
from rest_framework import fields, serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields='__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Catagory
        fields='__all__'


