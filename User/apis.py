import http

from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .helpers import generateOTP
from twilio.rest import Client
from .models import Address
from rest_framework import status
from .serializers import AddressSerializer

User = get_user_model()
class user(APIView):
   def get(self,request):
       userlist = User.objects.all()
       serializer = UserSerializer(userlist,many=True)
       return Response(serializer.data)

   def post(self, request):
       serializer = UserSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()

           user = User.objects.get(phone_number="01521332753")
           print(user)
           token_obj, _ = Token.objects.get_or_create(user=user)
           return Response({'data':serializer.data,'token':str(token_obj)})

       return Response(serializer.errors)
class SendOTP(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)


        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(phone_number=request.data['phone_number'])
            user.name = user.phone_number
            user.otp = generateOTP()
            user.save()
            return Response(f"OTP Send to {request.data['phone_number']} ")
        else:
            user = User.objects.get(phone_number=request.data['phone_number'])
            user.otp = generateOTP()
            user.save()
            return Response(f"OTP Send to {request.data['phone_number']} ")
        """account_sid = 'ACed6f2340b442f747403a7abadc8f4743'
        auth_token = '23a5cb7e6ba0e9b09281c4de70e8256c'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='+14348305596',
            body=f'Your Two step verifaction code is {user.otp}',
            to=user.phone_number
        )

        print(message.sid)"""

        return Response("Error")

class VerifyOTP(APIView):
     def post(self,request):
         try:
             user=User.objects.get(phone_number=request.data['phone_number'])
             if user.otp==request.data['otp']:
                 user.is_otp_verified=True
                 token_obj, _ = Token.objects.get_or_create(user=user)
                 user.save()
                 return Response({'name':user.name,'email':user.email,'gender':user.gender,'date_of_birth':user.date_of_birth,'phone_number':user.phone_number, 'token': str(token_obj)})
         except:
             return Response({"Wrong OTP"})
class UpdateUser(APIView):
    def post(self,request):
        token = request.data['token']
        print(token)
        user=User.objects.filter(auth_token__exact=token)


        if user.exists():

            if(request.data['name']):
                user.update(name=request.data['name'])
            if (request.data['email']):
                user.update(email=request.data['email'])
            if (request.data['date_of_birth']):
                user.update(date_of_birth=request.data['date_of_birth'])
            if (request.data['gender']):
                if request.data['gender']=='1':
                    user.update(gender=1)
                if request.data['gender']=='2':
                    user.update(gender=2)
                if request.data['gender']=='3':
                    user.update(gender=3)

            return Response({'name':user.first().name,'email':user.first().email,'phone_number':user.first().phone_number,
                             'gender':user.first().gender,'date_of_birth':user.first().date_of_birth,'token': str(token)})
        else:

            return Response({"status":404})
class UpdateAddress(APIView):
        def post(self, request):
            token = request.data['token']
            user = User.objects.filter(auth_token__exact=token)
            if user.exists():

                Address.objects.create(address=user.first(),street_address=request.data['street_address'],floor_no=request.data['floor_no'],apartment_no=request.data['apartment_no'])

                qs = Address.objects.filter(address=user.first())
                serializer = AddressSerializer(qs,many=True)

                return Response(serializer.data)
            return Response("invalid")

        def put(self, request, id):
            token = request.data['token']
            user = User.objects.filter(auth_token__exact=token)
            if user.exists():

               Address.objects.filter(pk=id).update(street_address=request.data['street_address'],floor_no=request.data['floor_no'], apartment_no=request.data['apartment_no'])
               qs = Address.objects.filter(pk=id)
               serializer = AddressSerializer(qs, many=True)





            return Response(serializer.data, status=status.HTTP_200_OK)

        def get(self, request):
            token = request.data['token']
            user = User.objects.filter(auth_token__exact=token)
            if user.exists():
                qs = Address.objects.filter(address=user.first())
                serializer = AddressSerializer(qs, many=True)
                return Response(serializer.data)
            return Response("Does Not Exist")

