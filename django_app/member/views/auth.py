import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpResponse

from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from member.pagination import PostPagination
from member.serializers import MyUserInfoSerializer, MyUserSerializer, LoginSerializer, ChangePasswordSerializer

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from utils import permissions

MyUser = get_user_model()

##
# view 는 '사용제에게 제공될 데이터를 보는 것을 의미한다.
#   '데이터가 어떻게 보이는가?'에 대한 것은 필요하지 않다.
#   '어떤 데이터가 보일것인가?'에 집중해야한다.
##


class SignUpView(APIView):
    """ 회원가입 """

    # serializer_class 는 generic 뷰에 사용되는 요소이다.
    # serializer_class = MyUserSerializer

    def post(self, request, format=None):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """ 일반 로그인 """

    def post(self, request, format=None):
        data = request.data.copy()
        data['user_type'] = 'd'
        print(data)
        serializer = LoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            ret = serializer.validated_data
        return Response(ret)


class FaceBookLoginView(APIView):
    """ 페이스북 로그인 """

    def post(self, request):
        token = request.data.get('token')

        if not token:
            raise APIException('Token require')

        self.debug_token(token)
        user_info = self.get_user_info(token=token)

        # 존재하면 유저정보 가져오고 아니면 get_or_create_facebook_user 메서드 실행
        if MyUser.objects.filter(username=user_info['id']).exists():
            user = MyUser.obejcts.get(username=user_info['id'])
        else:
            user = MyUser.objects.get_or_create_facebook_user(user_info)

        data = dict(username=user.username)
        data['user_type'] = 'f'
        serializer = LoginSerializer(user, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            ret = serializer.validated_data
        return Response(ret)

    def debug_token(self, token):
        app_access_token = '{}|{}'.format(
            settings.FACEBOOK_APP_ID,
            settings.FACEBOOK_SECRET_CODE,
        )

        debug_token_url = 'https://graph.facebook.com/debug_token'
        debug_token_url_params = {
            'input_token': token,
            'access_token': app_access_token
        }

        response = requests.get(debug_token_url, debug_token_url_params)
        result = response.json()

        if 'error' in result['data']:
            raise APIException('Token Invalid')
        else:
            return result

    def get_user_info(self, token):
        url_user_info = 'https://graph.facebook.com/v2.9/me'
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
        return result


class MyProfileView(APIView):
    """ 마이페이지 조회/수정/삭제 """

    permission_classes = (IsAuthenticated, )

    # API 뷰에 적합한 접근 제한 방식이 아니다.
    # def get(self, request, user_pk):
    #     user = MyUser.objects.get(pk=user_pk)
    #     serializer = MyUserSerializer(user)
    #     user_data = JSONRenderer().render(serializer.data)
    #
    #     if not request.user.is_authenticated and request.user.pk != user_pk:
    #         login_url = '/member/login/'
    #         redirect_url = login_url + '?next=' + request.get_full_path()
    #         return redirect(redirect_url)
    #     return Response(serializer.data)

    def get(self, request, user_pk):
        user = MyUser.objects.get(pk=user_pk)
        serializer = MyUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, user_pk, format=None):
        user = MyUser.objects.get(pk=user_pk)

        # 시리얼라이저 모델에 속하고 필수 필드이면 반드시 필요한 정보이므로 아래와 같은 작업을 한다.
        # 하지만 `partial=True`를 하면 이 또한 안 해도 되는 작업이다.
        data = request.data.copy()
        data['username'] = user.username
        data['password'] = user.password
        data['confirm_password'] = user.password

        serializer = MyUserSerializer(user, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print('I want to pass this validation test!')
        return Response(serializer.data)

    def delete(self, request, user_pk, format=None):
        user = MyUser.objects.get(pk=user_pk)
        user.delete()
        return HttpResponse('Hello Delete Request')

    # URL keyword argument, 기본은 pk
    # lookup_field = 'username'

    # @method_decorator(login_required(login_url='/member/login/'))
    # def dispatch(self, request, *args, **kwargs):
    #     return super(ChangeMyProfileView, self).dispatch(*args, **kwargs)


class ChangePasswordView(APIView):

    def patch(self, request, user_pk):
        user = MyUser.objects.get(pk=user_pk)

        # `partial=True`를 지정함으로써 필요없는 작업이 된다.
        # data = request.data.copy()
        # data['username'] = user.username
        serializer = ChangePasswordSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


class TokenUserInfoAPIView(APIView):
    def post(self, request):
        token_string = request.data.get('token')
        try:
            token = Token.objects.get(key=token_string)
        except Token.DoesNotExist:
            raise APIException('token invalid')
        user = token.user
        return Response(MyUserSerializer(user).data)


class MyUserList(generics.ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserInfoSerializer
    pagination_class = PostPagination


class MyUserDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk=None):
        return Response(MyUserSerializer(request.user).data)


# class MyUserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     ViewSet
#         - MyUserList + MyUserDetail = MyUserViewSet
#         - URL 구조는 기본 관례에 따라 자동으로 설정된다.
#     """
#     queryset = MyUser.objects.all()
#     serializer_class = MyUserSerializer
