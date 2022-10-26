from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CartSerializer
from .models import Cart
from User.models import User
from inventory.models import Product
class cart(APIView):

    def get(self,request):
        uuid=User.objects.get(auth_token='24a59d0720b85716f84f664ac5580f7754b03a96')
        qs=Cart.objects.filter(user__pk=uuid.id)
        serializer = CartSerializer(qs, many=True)
        list=[]
        for obj in qs:
            dict={}
            dict["id"]=obj.id
            dict["quantity"] = obj.quantity
            dict["user_id"] = obj.user.id
            dict["product_price"] = obj.item.price
            dict["product_name"]=obj.item.title
            dict["total_price"]=obj.quantity*obj.item.price

            list.append(dict)







        return Response(list)