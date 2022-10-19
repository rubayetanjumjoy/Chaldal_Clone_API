from .models import User
from .models import Address
from rest_framework import fields, serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields=['email','name','phone_number','gender','date_of_birth']
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model =Address
        fields='__all__'