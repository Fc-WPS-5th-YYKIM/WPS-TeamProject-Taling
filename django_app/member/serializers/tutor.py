from django.contrib.auth import get_user_model
from rest_framework import serializers

from member.models import Tutor, Certification

MyUser = get_user_model()


class TutorRegisterSerializer(serializers.ModelSerializer):
    # basic_info = MyUserUpdateSerializer(many=False)
    my_photo = serializers.ImageField(required=True)
    nickname = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    cert_name = serializers.ListField(
        child=serializers.CharField(),
        # write_only=True
    )
    cert_photo = serializers.ListField(
        child=serializers.ImageField(),
        # write_only=True
    )

    class Meta:
        model = Tutor
        fields = (
            'cert_type',
            'school',
            'major',
            'status_type',
            # 'identification',
            'my_photo',
            'nickname',
            'phone',
            'cert_name',
            'cert_photo',
        )

    def validate_my_photo(self, data):
        print(data)
        return data

    def validate_nickname(self, data):
        print(data)
        return data

    def validate_phone(self, data):
        print(data)
        return data

    def validate_cert_name(self, data):
        print(data)
        return data

    def validate_cert_photo(self, data):
        print(data)
        return data

    def validate(self, data):
        return data
