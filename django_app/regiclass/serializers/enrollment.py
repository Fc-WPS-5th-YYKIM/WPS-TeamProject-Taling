from django.contrib.auth import get_user_model
from rest_framework import serializers

from member.models import MyUser, Tutor
from regiclass.models import Lecture, Enrollment


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = (
            'username'
        )


class ProcessGuideSerializer(serializers.ModelSerializer):
    username = MyUserSerializer()

    class Meta:
        model = Tutor
        fields = (
            'username',
            'author.nickname',
        )


class CheckLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = (
            # 'location2',
            # 'class_weekday',
            # 'class_time',

        )