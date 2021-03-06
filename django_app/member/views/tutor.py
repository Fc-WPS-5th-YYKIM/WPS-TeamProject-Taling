from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Tutor, Certification
from member.serializers import TutorRegisterSerializer
from member.serializers.tutor import TutorSerializer
from utils.permissions import IsOwnerOrReadOnly

MyUser = get_user_model()

__all__ = (
    'TutorRegister',
    'TutorDetailView',
)


class TutorRegister(APIView):
    permission_classes = (IsOwnerOrReadOnly, )

    def post(self, request):
        serializer = TutorRegisterSerializer(data=request.data)

        user = MyUser.objects.get(pk=request.user.id)

        if serializer.is_valid(raise_exception=True):
            instance = serializer.validated_data
            user.info_update(
                my_photo=instance['my_photo'],
                nickname=instance['nickname'],
                phone=instance['phone'],
            )

            tutor, created = Tutor.objects.get_or_create(
                author=user,
                cert_type=instance['cert_type'],
                school=instance['school'],
                major=instance['major'],
                status_type=instance['status_type'],
            )

            for i in range(len(instance['cert_name'])):
                Certification.objects.get_or_create(
                    tutor=tutor,
                    cert_name=instance['cert_name'][i],
                    cert_photo=instance['cert_photo'][i]
                )

            return Response(TutorSerializer(tutor).data)


class TutorDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, tutor_pk):
        tutor = Tutor.objects.get(pk=tutor_pk)
        serializer = TutorSerializer(tutor)
        return Response(serializer.data)

    def put(self, request, tutor_pk):
        tutor = Tutor.objects.get(pk=tutor_pk)
        user = tutor.author
        serializer = TutorRegisterSerializer(instance=tutor, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.validated_data
            user.info_update(
                my_photo=instance.get('my_photo', user.my_photo),
                nickname=instance.get('nickname', user.nickname),
                phone=instance.get('phone', user.phone),
            )
            serializer.save()
            return self.get(request, tutor_pk)

    def delete(self, request, tutor_pk):
        tutor = Tutor.objects.get(author=request.user)
        tutor.delete()
        return HttpResponse('Delete')
