
from django.contrib import admin
from django.urls import path,include
from .apis import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [

    path('user/',user.as_view(),name='user' ),
    path('updateuser/',UpdateUser.as_view(),name='updateuser' ),

    path('sendotp/', SendOTP.as_view(), name='SendOTP'),
    path('verifyotp/', VerifyOTP.as_view(), name='verifyotp'),
    path('updateaddress/', UpdateAddress.as_view(), name='address'),
    path('updateaddress/<int:id>', UpdateAddress.as_view(), name='addressbyid')

]
