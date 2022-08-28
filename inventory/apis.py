from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from .ducuments import *
import json
import requests
class ProductList(APIView):
    def get(self,request):
        qs=Product.objects.all()

        return Response(ProductSerializer(qs,many=True,context={'request': request}).data)
class SearchProduct(APIView):

    def get (self,request):
          searchkey = request.GET.get('q')

          search=PostDocumentProduct.search().query('multi_match', query=searchkey,fields=['title',],fuzziness='auto')
          list=[]

          for hit in search:
              dict = {}
              dict['id']=hit.id
              dict['title']=hit.title
              dict['description']=hit.description
              dict['image']=f"http://127.0.0.1:8000{hit.image}"
              dict['price']=hit.price
              list.append(dict)

          

          return Response(list)

