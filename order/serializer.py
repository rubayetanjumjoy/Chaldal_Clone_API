from .models import Cart
from rest_framework import fields, serializers
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model =Cart
        fields='__all__'