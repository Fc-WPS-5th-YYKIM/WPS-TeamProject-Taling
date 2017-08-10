from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import permissions, status
from django.core import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Tutor
from regiclass.models import Lecture, ClassLocation, LecturePhoto
from regiclass.serializers import LectureListSerializer, LectureMakeSerializer

MyUser = get_user_model()


class LectureMake(APIView):
    serializer_class = LectureMakeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        user = MyUser.objects.get(pk=request.user.id)
        if serializer.is_valid():
            tutor = Tutor.objects.get(author=user)
            instance = serializer.validated_data

            lecture, lecture_created = Lecture.objects.get_or_create(
                tutor=tutor,
                title=instance['title'],
                category=instance['category'],
                class_type=instance['class_type'],
                min_member=instance['min_member'],
                max_member=instance['max_member'],
                cover_photo=instance['cover_photo'],
                tutor_intro=instance['tutor_intro'],
                class_intro=instance['class_intro'],
                target_intro=instance['target_intro'],
                price=instance['price'],
                basic_class_time=instance['basic_class_time'],
                total_count=instance['total_count'],
                youtube_url1=instance['youtube_url1'],
                youtube_url2=instance['youtube_url2'],
                region_comment=instance['region_comment'],
                notice=instance['notice'],
            )

            if lecture_created:
                for i in range(len(instance['location1'])):
                    ClassLocation.objects.get_or_create(
                        lecture=lecture,
                        location1=instance['location1'][i],
                        location2=instance['location2'][i],
                        location_option=instance['location_option'][i],
                        location_detail=instance['location_detail'][i],
                        location_etc_type=instance['location_etc_type'][i],
                        location_etc_text=instance['location_etc_text'][i],
                        class_weekday=instance['class_weekday'][i],
                        class_time=instance['class_time'][i],
                    )

                for j in range(len(instance['photo_type'])):
                    LecturePhoto.objects.get_or_create(
                        lecture=lecture,
                        photo_type=instance['photo_type'][j],
                        photo=instance['photo'][j],
                    )

            return Response({'result': status.HTTP_201_CREATED})
        return Response({'result': status.HTTP_400_BAD_REQUEST})


class LectureList(APIView):
    serializer_class = LectureListSerializer

    def get(self, request):
        search_text = request.GET.get('search_text', '')
        order_by = request.GET.get('ordering', '-modify_date')
        lecture_list = Lecture.objects.filter(
            (Q(title__contains=search_text) | Q(tutor__author__nickname__contains=search_text))
        ).order_by(order_by)
        serializer = self.serializer_class(lecture_list, many=True)
        return Response(serializer.data)


class LectureDetail(APIView):
    serializer_class = LectureListSerializer

    def post(self, request):
        lecture_id = request.POST.get('lecture_id')
        lecture = Lecture.objects.get(pk=lecture_id)
        serializer = self.serializer_class(lecture)
        return Response(serializer.data)
