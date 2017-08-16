from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Tutor
from regiclass.serializers.enrollment import ProcessGuideSerializer

MyUser = get_user_model()


class TalenteGuideView(APIView):
    def get(self, request, slug):
        user = MyUser.objects.get(pk=request.user.pk)
        tutor = Tutor.objects.get(slug=slug)

        serializer = ProcessGuideSerializer(user, tutor)
        return Response(serializer.data)