from .models import User
from rest_framework import fields, serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields='__all__'