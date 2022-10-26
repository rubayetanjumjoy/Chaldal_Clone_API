from .models import cart
from rest_framework import fields, serializers
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model =cart
        fields='__all__'