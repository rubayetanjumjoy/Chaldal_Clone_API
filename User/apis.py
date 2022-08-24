
from User.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .helpers import generateOTP
from twilio.rest import Client
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
        user.otp = generateOTP()
        user.name=user.phone_number
        user.save()
        """account_sid = 'ACed6f2340b442f747403a7abadc8f4743'
        auth_token = '23a5cb7e6ba0e9b09281c4de70e8256c'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='+14348305596',
            body=f'Your Two step verifaction code is {user.otp}',
            to=user.phone_number
        )

        print(message.sid)"""

        return Response(f"OTP Send to {request.data['phone_number']} ")

class VerifyOTP(APIView):
     def post(self,request):
         try:
             user=User.objects.get(phone_number=request.data['phone_number'])
             if user.otp==request.data['otp']:
                 user.is_otp_verified=True
                 token_obj, _ = Token.objects.get_or_create(user=user)
                 user.save()
                 return Response({'name':user.name,'phone_number':user.phone_number, 'token': str(token_obj)})
         except:
             return Response({"Wrong OTP"})

