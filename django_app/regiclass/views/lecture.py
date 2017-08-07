from rest_framework import generics, permissions

from ..permissions import IsOwnerOrReadOnly


class EnrollmentList(generics.ListCreateAPIView):

    ##
    # pre_save() 오버라이드
    #   - MyUser 와 Lecture 가 연결
    ##
    def pre_save(self, obj):
        obj.owner = self.request.user

    ##
    # 유효한 user 만 Lecture 를 생성, 수정, 삭제가 가능하도록 권한 확인 추가
    ##
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)


class EnrollmentDetail(generics.RetrieveUpdateDestroyAPIView):

    def pre_save(self, obj):
        obj.owner = self.request.user

    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,
                           IsOwnerOrReadOnly,)