from rest_framework.views import APIView
from rest_framework.response import Response

from User.models import User
from inventory.models import Product
from .serializer import OrderSerializer
from .models import orderItem
import requests
class Order(APIView):
    def get(self,request):
        qs=orderItem.objects.filter(user__auth_token="24a59d0720b85716f84f664ac5580f7754b03a96")
        serializer=OrderSerializer(qs,many=True)
        list=[]
        total_price=0
        for data in qs:
            dict={}
            dict['id']=data.id
            dict['quantity']=data.quantity

            user={}
            user["id"] = data.user.id
            user["email"]=data.user.email
            user["name"]=data.user.name
            user["phone_number"]=data.user.phone_number
            user["gender"] = data.user.gender
            user["date_of_birth"] = data.user.date_of_birth
            dict["user"]=user
            product={}
            product["id"] = data.product.id
            product["title"] = data.product.title
            product["description"] = data.product.description

            product["price"] = data.product.price
            product["catagory_id"] = data.product.catagory.id
            product["catagory"] = data.product.catagory.name

            dict["product"] = product
            total_price=total_price+(data.product.price*data.quantity)

            total = {"total_items_price": total_price, "delevery_charge": 30, "total_price": total_price+ 30}


            list.append(dict)
            list.append(total)
        return Response(list)

    def post(self, request):
        token="24a59d0720b85716f84f664ac5580f7754b03a96"
        uu=User.objects.get(auth_token=token)
        prod=Product.objects.get(pk=2)
        s=orderItem.objects.create(user=uu,product=prod,quantity=3)
        return Response("ok")