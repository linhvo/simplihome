import logging
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from simplihome.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from rest_framework import permissions
from rest_framework import generics

logger = logging.getLogger(__name__)

class UserList(APIView):
    queryset = User.objects.all()

    def get(self, request):
        users = self.queryset
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        data = request.data
        try:
            user = User.objects.create_user(username=data['username'], password=data['password'], email=data['email'])
            user.save()
            token=Token.objects.create(user=user)
            logger.info(token)
        except Exception as ex:
            return HttpResponse('Cannot save user! Error: %s'% ex)

        serializer = UserSerializer(user)
        return Response(serializer.data, status=201)

class UserDetail(APIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get_object(self, pk):
        try:
            return self.queryset.get(pk=pk)
        except User.DoesNotExist:
            return Http404

    def get(self, request, pk):
            user = self.get_object(pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)

    def put(self, request, pk):
        data = request.data
        user = self.get_object(pk)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        if password:
            user.set_password(data['password'])
        if username:
            user.username = username
        if email:
            user.email = email
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
