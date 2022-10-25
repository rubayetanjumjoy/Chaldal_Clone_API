

from django.urls import path,include
from .apis import *




urlpatterns = [
    path('cartitem/', cart.as_view(), name='cart'),

]
