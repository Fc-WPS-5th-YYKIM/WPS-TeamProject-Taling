from django.contrib.auth import get_user_model
from rest_framework import serializers

from member.models import MyUser, Tutor
from regiclass.models import Lecture, Enrollment


class ProcessGuideSerializer(serializers.Serializer):
    username = serializers.CharField()
    tutor_nickname = serializers.CharField()


class CheckLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = (
            'location',


        )