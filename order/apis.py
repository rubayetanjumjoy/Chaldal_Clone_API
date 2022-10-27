from rest_framework.views import APIView
from rest_framework.response import Response

from User.models import User
from inventory.models import Product
from .serializer import OrderSerializer
from .models import orderItem
from User.serializers import UserSerializer
from inventory.serializers import ProductSerializer
import uuid
import requests
class Order(APIView):
    def get(self,request):

        qs=orderItem.objects.filter(user__auth_token=request.data['token'])
        serializer=OrderSerializer(qs,many=True)
        shipid=orderItem.objects.filter(user__auth_token=request.data['token']).values('shipment_id').distinct()
        list = []

        for id in shipid:
            dict={}
            dict["shipment_id"]=id["shipment_id"]

            qs = orderItem.objects.filter(shipment_id=id['shipment_id'])
            list2=[]
            list.append(dict)

            for data in qs:
                totalprice=0
                dict2={
                    "id":data.id,
                    "quantity":data.quantity,
                    "total_price" : data.total_price,

                    "product" : ProductSerializer(data.product).data,
                    "user" : UserSerializer(data.user).data,

                }

                list2.append(dict2)

            dict["items"]=list2


        '''
       
        shipid=asd
        {
        for d in qs:
            dict = {}
            dict['id'] = d.id
            dict['quantity'] = d.quantity
            dict['total_price'] = d.total_price

            dict['product'] = ProductSerializer(d.product).data
            dict['user'] = UserSerializer(d.user).data


            list.append(dict)
        '''
        return Response(list)

    def post(self, request):
        payload=request.data['payload']
        print(payload)
        list = []
        total_price = 0

        shipment_id = uuid.uuid4().hex[:8]
        dict = {}
        dict["shipment_id"] = shipment_id
        list.append(dict)

        for data in payload:
            token=data["token"]
            prodid=data['product_id']
            quantity=data['quantity']

            uu = User.objects.get(auth_token=token)
            prod = Product.objects.get(pk=prodid)
            data = orderItem.objects.create(user=uu, product=prod, quantity=quantity,shipment_id=shipment_id,total_price=prod.price*quantity)
            qs = orderItem.objects.filter(shipment_id=shipment_id)
            list2=[]

            for data in qs:

                dict2 = {
                    "id": data.id,
                    "quantity": data.quantity,
                    "total_price": data.total_price,

                    "product": ProductSerializer(data.product).data,
                    "user": UserSerializer(data.user).data,

                }

                list2.append(dict2)


            dict["items"] = list2

        return Response(list)