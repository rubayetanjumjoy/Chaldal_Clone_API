from itertools import product

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from .ducuments import *
import json
import subprocess
import requests
class ProductList(APIView):
    def get(self,request):
        qs=Product.objects.all()

        return Response(ProductSerializer(qs,many=True,context={'request': request}).data)
class ProductListbyCatagory(APIView):
      def get(self,request,catagory):
          qs= Product.objects.filter(catagory__slug = catagory)

          return Response(ProductSerializer(qs, many=True, context={'request': request}).data)
class CatagoryList(APIView):
    def get(self, request):
        qs=Catagory.objects.all()
        print("asd")
        serializer=CategorySerializer(qs,many=True)
        return Response(serializer.data)

class SearchProduct(APIView):

    def get (self,request):
          searchkey = request.GET.get('q')
          qs = Product.objects.filter(title__contains=searchkey)


          serializer = ProductSerializer(qs, many=True, context={'request': request}).data

          """
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
          """
          '''
          elasticquery = {"query": {"fuzzy": {"title": {"value": f"{searchkey}", "fuzziness": 2}}}}
          response = requests.get("http://3.0.95.128:9200/products/_search", json=elasticquery)

          list = []
          elasticjson = response.json()
          for row in elasticjson['hits']['hits']:
              dict = {}
              dict['id'] = row['_source']['id']
              dict['title'] = row['_source']['title']
              dict['description'] = row['_source']['description']
              dict['image'] = f"http://18.139.114.65:8000{row['_source']['image']}"
              dict['price'] = row['_source']['price']
              list.append(dict)

          '''

          return Response(serializer)
class os(APIView):
    def get(self,request):

        result=subprocess.run('ls', shell=True,capture_output=True)
        if(result.returncode==0):
            return Response(result.stdout)


        return Response('error')




