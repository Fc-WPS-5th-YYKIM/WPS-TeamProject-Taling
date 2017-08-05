from django.contrib.auth import get_user_model
from rest_framework import serializers

from member.models import Tutor, Certification

MyUser = get_user_model()


class TutorRegisterSerializer(serializers.ModelSerializer):
    # basic_info = MyUserUpdateSerializer(many=False)
    # my_photo =
    nickname = serializers.CharField()
    phone = serializers.CharField()
    cert_name = serializers.ListField(
        child=serializers.CharField(),
        write_only=True
    )
    cert_photo = serializers.ListField(
        # child=serializers.ImageField(),
        child=serializers.CharField(),
        write_only=True
    )

    class Meta:
        model = Tutor
        fields = (
            'cert_type',
            'school',
            'major',
            'status_type',
            # 'identification',
            # 'my_photo',
            'nickname',
            'phone',
            'cert_name',
            'cert_photo',
        )

    def validate_cert_name(self, data):
        return data

    def validate_cert_photo(self, data):
        return data

    # def validate_my_photo(self, data):
    #     return data

    def validate_nickname(self, data):
        if not data['nickname']:
            raise serializers.ValidationError(
                '별명을 입력해주세요.'
            )
        return data

    def validate_phone(self, data):
        if not data['phone']:
            raise serializers.ValidationError(
                '핸드폰 번호를 입력해주세요.'
            )
        return data

    def validate(self, data):
        # cert_type = data['cert_type']
        # schooal = data['school']
        # major = data['major']
        # status_type = data['status_type']
        return data


