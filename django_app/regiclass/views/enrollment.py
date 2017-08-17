from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Tutor
from member.serializers import MyUserSerializer
from regiclass.serializers.enrollment import ProcessGuideSerializer

MyUser = get_user_model()


class TalenteGuideView(APIView):
    def get(self, request, slug):
        user = MyUser.objects.get(pk=request.user.pk)
        tutor = Tutor.objects.get(slug=slug)
        data = {
            'username': request.user.username,
            'tutor_nickname': tutor.author.nickname
        }

        MyUserSerializer(user)
        tutor_serializer = ProcessGuideSerializer(data=data)

        if tutor_serializer.is_valid(raise_exception=True):
            return Response(tutor_serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)