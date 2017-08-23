from rest_framework import serializers

from member.models import MyUser, Tutor
from regiclass.models import Enrollment, Lecture


class MyUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = (
            'my_photo',
            'nickname',
        )


class TutorInfoSerializer(serializers.ModelSerializer):
    author = MyUserInfoSerializer()

    class Meta:
        model = Tutor
        fields = (
            'pk',
            'author',
        )


class LectureInfoSerializer(serializers.ModelSerializer):
    tutor = TutorInfoSerializer()
    user = serializers.SerializerMethodField('get_info')

    class Meta:
        model = Lecture
        fields = (
            'title',
            'tutor',
            'user',
        )

    def get_info(self, obj):
        return self.context['user']


class EnrollmentSerializer(serializers.ModelSerializer):\

    class Meta:
        model = Enrollment
        fields = (
            'to_tutor',
        )

# class ProcessGuideSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     tutor_nickname = serializers.CharField()
#     tutor_photo = serializers.ImageField()

# class MyUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = settings.AUTH_
#         fields = ('username')


# class CheckLocationSerializer(serializers.ModelSerializer):
#     extra = serializers.SerializerMethodField('get_info')
#
#     class Meta:
#         model = ClassLocation
#         fields = (
#             'class_weekday',
#             # 'location2',
#             'class_time',
#             'location_detail',
#             'location_etc_text',
#
#             'extra',
#         )
#
#     def get_info(self, obj):
#         return self.context['extra']
#
#     def validate(self, data):
#         return data
#
#
# class ApplyMyTalentSerializer(serializers.ModelSerializer):
#     level = serializers.CharField(required=True)
#     career = serializers.CharField(required=True)
#     to_tutor = serializers.CharField(required=True)
#
#     class Meta:
#         model = Enrollment
#         fields = (
#             'level',
#             'career',
#             'to_tutor',
#         )
#
#     def update(self, instance, validated_data):
#         instance.level = validated_data.get('level', instance.level)
#         instance.career = validated_data.get('career', instance.career)
#         instance.to_tutor = validated_data.get('to_tutor', instance.to_tutor)
#         instance.save()
#
#         return instance
#
#     def validate(self, data):
#         return data
#
#
# class ClassPaymentSerializer(serializers.ModelSerializer):
#     pay_method = serializers.CharField(required=True)
#
#     class Meta:
#         model = Enrollment
#         fields = (
#             'pay_method',
#             'remitter',
#         )