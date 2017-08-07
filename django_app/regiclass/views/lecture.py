from django.db.models import Q
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from regiclass.models import Lecture
from regiclass.serializers import LectureSerializer


class LectureMake(APIView):
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = LectureSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(tutor=request.user.tutor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LectureList(APIView):
    serializer_class = LectureSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request):
        search_text = request.GET.get('search_text', '')
        lecture_list = Lecture.objects.filter(
            (Q(title__contains=search_text) | Q(tutor__author__nickname__contains=search_text))
            # &
            # (Q(title__contains=search_text))
        )
        serializer = self.serializer_class(lecture_list, many=True)
        return Response(serializer.data)
