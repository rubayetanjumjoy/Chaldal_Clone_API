
from rest_framework import fields, serializers
from .models import orderItem
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model =orderItem
        fields='__all__'