from django.contrib.auth import get_user_model
from rest_framework import generics

from member.serializers import MyUserSerializer

MyUser = get_user_model()


class MyUserList(generics.ListAPIView):
    model = MyUser
    serializer_class = MyUserSerializer


class MyUserDetail(generics.RetrieveAPIView):
    model = MyUser
    serializer_class = MyUserSerializer


