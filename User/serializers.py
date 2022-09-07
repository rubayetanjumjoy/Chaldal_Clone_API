from .models import User
from .models import Address
from rest_framework import fields, serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields='__all__'
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model =Address
        fields='__all__'