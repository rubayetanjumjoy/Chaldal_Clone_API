

from django.urls import path,include
from .apis import *

urlpatterns = [

    path('products/',ProductList.as_view(),name='product' ),
    path('search/', SearchProduct.as_view(), name='search'),

]
