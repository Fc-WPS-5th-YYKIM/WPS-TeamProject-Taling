import requests
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import redirect

from rest_framework import generics, status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from member.pagination import PostPagination
from member.serializers import MyUserInfoSerializer, MyUserSerializer, TalingLoginSerializer
from utils.access_token_test import access_token_test, debug_token

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

MyUser = get_user_model()

##
# view 는 '사용제에게 제공될 데이터를 보는 것을 의미한다.
#   '데이터가 어떻게 보이는가?'에 대한 것은 필요하지 않다.
#   '어떤 데이터가 보일것인가?'에 집중해야한다.
##


class SignUpView(APIView):
    serializer_class = MyUserSerializer

    # def get_object(self, pk):
    #     try:
    #         return Snippet.objects.get(pk=pk)
    #     except Snippet.DoesNotExist:
    #         raise Http404

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    serializer_class = TalingLoginSerializer

    def post(self, request, format=None):

        serializer = TalingLoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            token_key = serializer.validated_data

        return Response({'token': token_key})


class QueryMyProfile(APIView):
    """마이페이지 조회"""
    serializer_class = MyUserSerializer

    def get(self, request, user_pk):
        user = MyUser.objects.get(pk=user_pk)
        serializer = MyUserSerializer(user)
        # user_data = JSONRenderer().render(serializer.data)

        if not request.user.is_authenticated and request.user.pk != user_pk:
            login_url = '/member/login/'
            redirect_url = login_url + '?next=' + request.get_full_path()
            return redirect(redirect_url)
        return Response(serializer.data)


class EditOrDeleteMyProfile(RetrieveUpdateDestroyAPIView):
    """마이페이지 수정/삭제"""
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

    # def get(self, request, pk):
    #     if not request.user.is_authenticated and request.user.pk != pk:
    #         login_url = '/member/login/'
    #         redirect_url = login_url + '?next=' + request.get_full_path()
    #         return redirect(redirect_url)
    def put(self, request, pk):
        print(request.data)
        serializer = MyUserSerializer(request.data)
        return HttpResponse('hello word')
    # URL keyword argument, 기본은 pk
    # lookup_field = 'username'

    # @method_decorator(login_required(login_url='/member/login/'))
    # def dispatch(self, request, *args, **kwargs):
    #     return super(ChangeMyProfileView, self).dispatch(*args, **kwargs)


class FaceBookLoginView(APIView):
    def get(self, request):
        access_token = access_token_test(request)
        print(access_token)
        debug_result = debug_token(access_token)
        print(debug_result)

        def get_user_info(user_id, token):
            url_user_info = 'https://graph.facebook.com/v2.9/{user_id}'.format(user_id=user_id)
            url_user_info_params = {
                'access_token': token,
                'fields': ','.join([
                    'id',
                    'name',
                    'email',
                    'picture',
                ])
            }
            response = requests.get(url_user_info, params=url_user_info_params)
            result = response.json()
            print(result)
            return result

        user_info = get_user_info(user_id=debug_result['data']['user_id'], token=access_token)
        user = MyUser.objects.get_or_create_facebook_user(user_info)
        token, created = user.get_user_token(user.pk)
        return Response({'token': token.key})


class MyUserList(generics.ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserInfoSerializer
    pagination_class = PostPagination


class MyUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserInfoSerializer


# class MyUserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     ViewSet
#         - MyUserList + MyUserDetail = MyUserViewSet
#         - URL 구조는 기본 관례에 따라 자동으로 설정된다.
#     """
#     queryset = MyUser.objects.all()
#     serializer_class = MyUserSerializer
