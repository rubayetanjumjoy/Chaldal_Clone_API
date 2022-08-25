from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from .ducuments import PostDocument
import json
import requests
class ProductList(APIView):
    def get(self,request):
        qs=Product.objects.all()

        return Response(ProductSerializer(qs,many=True,context={'request': request}).data)
class SearchProduct(APIView):

    def get (self,request):
        searchkey=request.GET.get('q')
        print(searchkey)
        elasticquery={   "query": {     "fuzzy": {       "title": {"value":f"{searchkey}","fuzziness":2}   }   } }
        response = requests.get("http://192.168.100.199:9200/products/_search",json=elasticquery)
        dict={}
        list=[]
        elasticjson= response.json()
        for row in elasticjson['hits']['hits']:
            dict['title']=row['_source']['title']
            dict['description'] =row['_source']['description']
            dict['image'] =f"http://127.0.0.1:8000{row['_source']['image']}"
            dict['price'] =row['_source']['price']
            list.append(dict)
        return Response(list)

