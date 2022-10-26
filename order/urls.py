

from django.urls import path,include
from .apis import *




urlpatterns = [
    path('order/', Order.as_view(), name='cart'),

]
