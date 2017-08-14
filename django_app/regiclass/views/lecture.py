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
            try:
                tutor = Tutor.objects.get(author=user)
            except Tutor.DoesNotExist:
                return Response({'result': '튜터가 아닌 사용자는 강의를 개설할 수 없습니다'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            serializer.save(tutor=tutor)
            return Response({'result': status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
        return Response({'result': status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)


class LectureList(APIView):
    serializer_class = LectureListSerializer

    def post(self, request):
        search_text = request.POST.get('search_text', '')
        order_by = request.POST.get('ordering', '-modify_date')
        lecture_list = Lecture.objects.filter(
            (Q(title__contains=search_text) | Q(tutor__author__nickname__contains=search_text))
        ).order_by(order_by)
        serializer = self.serializer_class(lecture_list, many=True)
        return Response(serializer.data)


class LectureDetail(APIView):
    serializer_class = LectureListSerializer

    def post(self, request):
        lecture_id = request.POST.get('lecture_id')
        try:
            lecture = Lecture.objects.get(pk=lecture_id)
        except Lecture.DoesNotExist:
            return Response({'result': '해당하는 강의 정보가 없습니다.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = self.serializer_class(lecture)
        return Response(serializer.data)
