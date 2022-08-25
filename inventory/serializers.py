from .models import Product
from rest_framework import fields, serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields='__all__'

