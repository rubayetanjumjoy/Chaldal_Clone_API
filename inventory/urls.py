

from django.urls import path,include
from .apis import *

urlpatterns = [

    path('products/',ProductList.as_view(),name='product' ),
    path('products/catagorylist', CatagoryList.as_view(), name='catagroylist'),

    path('products/<str:catagory>',ProductListbyCatagory.as_view(),name='catagroy' ),
    path('search/', SearchProduct.as_view(), name='search'),
    path('os/', os.as_view(), name='os'),

]
