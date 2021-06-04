from rest_framework.views import APIView
from .models import UsersContact, UserSpam
from .serializers import UserContactSerializer, UserSpamSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
import io
from rest_framework.parsers import JSONParser
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class UserList(APIView):
    """
    Contain all the contact sync from the registered user
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user_contact = UsersContact.objects.all()
        serialize = UserContactSerializer(user_contact, many=True)
        return Response(serialize.data)

    def post(self, request, format=None):
        serialize = UserContactSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


class SpamUser(APIView):
    """
    Contain all the spam number and the user who declare it spam
    Post -> Add new number to spam and the user who declare it
    GET -> Return the count of user who declare it as spam
    """

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        # import pdb
        # pdb.set_trace()
        request.data['user'] = request.user.id
        serialize = UserSpamSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        json_data = request.body
        stream = io.BytesIO(json_data)
        try:
            context = JSONParser().parse(stream)
        except:
            return JsonResponse({'msg': 'Invalid Json'}, status=400)

        phone = context.get('phone')

        if phone is None:
            return JsonResponse({'msg': 'Phone number not provided!!'}, status=400)

        count = UserSpam.objects.filter(phone=context.get('phone')).count()
        return JsonResponse({'phone': context.get('phone'), 'Count': count})

