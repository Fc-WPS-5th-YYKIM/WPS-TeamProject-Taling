import datetime

from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from regiclass.models import Lecture, Enrollment
from regiclass.serializers.enrollment import EnrollmentSerializer, LectureInfoSerializer

MyUser = get_user_model()


class EnrollmentView(APIView):
    def get(self, request, lecture_pk):
        lecture = Lecture.objects.get(pk=lecture_pk)
        serializer = LectureInfoSerializer(lecture)
        return Response(serializer.data)

    def post(self, request, lecture_pk):
        user = MyUser.objects.get(pk=request.user.pk)
        lecture = Lecture.objects.get(pk=lecture_pk)
        serializer = EnrollmentSerializer(lecture, data=request.data)
        if serializer.is_valid(raise_exception=True):
            Enrollment.objects.get_or_create(
                user=user,
                lecture=lecture,
                to_tutor=serializer.validated_data['to_tutor']
            )
            return self.get(request, lecture_pk)


# class TalenteGuideView(APIView):
#     def get(self, request, slug):
#         lecture = Lecture.objects.get(slug=slug)
#         tutor = lecture.tutor
#         data = {
#             'username': request.user.username,
#             'tutor_nickname': tutor.author.nickname,
#             'tutor_photo': tutor.author.my_photo,
#         }
#
#         serializer = ProcessGuideSerializer(data=data)
#
#         if serializer.is_valid(raise_exception=True):
#             return Response(serializer.data)
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#
# class CheckLocationView(APIView):
#     def get(self, request, slug):
#         user = MyUser.objects.get(pk=request.user.pk)
#         lecture = Lecture.objects.get(slug=slug)
#         tutor = lecture.tutor
#         class_location = ClassLocation.objects.filter(lecture=lecture)
#
#         context = {
#             'extra': {
#                 'username': user.username,
#                 'tutor_nickname': tutor.author.nickname,
#                 'tutor_photo': tutor.author.my_photo.url,
#                 'tutor_intro': lecture.class_intro,
#             }
#         }
#         serializer = CheckLocationSerializer(instance=class_location, context=context)
#         return Response(serializer.data)
#
#     def post(self, request, slug):
#         context = {'extra': ''}
#         serializer = CheckLocationSerializer(data=request.data, context=context, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             data = serializer.data
#
#             enrollment, created = Enrollment.objects.get_or_create(
#                 user=request.user,
#                 lecture=Lecture.objects.get(slug=slug),
#                 # location=data.location2,
#                 class_day=data['class_weekday'],
#                 class_time=data['class_time'],
#             )
#             enrollment.save()
#             return Response('성공', status=status.HTTP_201_CREATED)
#         return HttpResponse('실패', status=status.HTTP_400_BAD_REQUEST)
#
#
# class ApplyMyTalentView(APIView):
#     def get(self, request, slug):
#         lecture = Lecture.objects.get(slug=slug)
#         tutor = lecture.tutor
#         ret = {
#             'tutor_nickname': tutor.author.nickname
#         }
#         return Response(ret)
#
#     def put(self, request, slug):
#         lecture = Lecture.objects.get(slug=slug)
#         enrollment = Enrollment.objects.get(lecture=lecture)
#         serializer = ApplyMyTalentSerializer(enrollment, data=request.data, partial=True)
#
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response('성공', status=status.HTTP_201_CREATED)
#         return HttpResponse('실패', status=status.HTTP_400_BAD_REQUEST)
#
#
# class StudentAuthView(APIView):
#     def get(self, request, slug):
#         user_phone = request.user.phone
#         ret = {
#             "user_phone": user_phone,
#         }
#         return Response(ret)
#
#
# class ClassPaymentView(APIView):
#     def get(self, request, slug):
#         lecture = Lecture.objects.get(slug=slug)
#         tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
#         due_to = tomorrow.strftime('%Y-%m-%d %H:%M')
#         ret = {
#             "price": lecture.price,
#             "due_to": due_to
#         }
#         return Response(ret)
#
#     def put(self, request, slug):
#         lecture = Lecture.objects.get(slug=slug)
#         enrollment = Enrollment.objects.get(lecture=lecture)
#         serializer = ClassPaymentSerializer(enrollment, data=request.data, partial=True)
#
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response('성공', status=status.HTTP_201_CREATED)
#         return HttpResponse('실패', status=status.HTTP_400_BAD_REQUEST)