from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework.views import APIView

from member.models import Tutor, Certification
from member.serializers import TutorRegisterSerializer

MyUser = get_user_model()


class TutorRegister(APIView):

    serializer_class = TutorRegisterSerializer
    # permission_classes =

    def post(self, request):
        serializer = TutorRegisterSerializer(data=request.data)

        user = MyUser.objects.get(pk=request.user.id)
        print(request.user)
        print(serializer.is_valid())

        if serializer.is_valid(raise_exception=True):
            print(serializer.data)
            instance = serializer.validated_data
            print("instance:", instance)
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

        return HttpResponse('helloworld')


