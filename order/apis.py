from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CartSerializer
from .models import Cart
from User.models import User
from inventory.models import Product
class cart(APIView):

    def get(self,request):
        uuid=User.objects.get(auth_token='24a59d0720b85716f84f664ac5580f7754b03a96')
        qs=Cart.objects.select_related('user').filter(pk=uuid.id)
        print(qs)



        serializer=CartSerializer(qs,many=True)

        return Response(serializer.data)