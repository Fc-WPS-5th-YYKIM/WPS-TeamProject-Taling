from rest_framework import generics

from member.pagination import PostPagination
from member.serializers.myclass import MyClassListSerializer
from regiclass.models import Enrollment


class MyClassListView(generics.ListAPIView):
    model = Enrollment
    serializer_class = MyClassListSerializer
    pagination_class = PostPagination

    def get_queryset(self):
        user = self.request.user
        return user.enrollment_set.all()

