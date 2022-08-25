

from django.urls import path,include
from .apis import *




urlpatterns = [

    path('cart/',cart.as_view(),name='cart' ),


]
