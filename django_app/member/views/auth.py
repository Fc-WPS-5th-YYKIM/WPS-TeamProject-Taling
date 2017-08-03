import requests
from django.contrib.auth import get_user_model

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from member.pagination import PostPagination
from member.serializers import MyUserSerializer, UserCreateSerializer
from utils.access_token_test import access_token_test, debug_token

MyUser = get_user_model()

##
# view 는 '사용제에게 제공될 데이터를 보는 것을 의미한다.
#   '데이터가 어떻게 보이는가?' 에 대한 것은 필요하지 않다.
#   '어떤 데이터가 보일것인가?' 에 집중해야한다.
##

class TalingSignUp(APIView):
    serializer_class = UserCreateSerializer
    # permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyUserList(generics.ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    pagination_class = PostPagination


class MyUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


# class MyUserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     ViewSet
#         - MyUserList + MyUserDetail = MyUserViewSet
#         - URL 구조는 기본 관례에 따라 자동으로 설정된다.
#     """
#     queryset = MyUser.objects.all()
#     serializer_class = MyUserSerializer
