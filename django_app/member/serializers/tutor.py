from django.contrib.auth import get_user_model
from rest_framework import serializers

from member.models import Tutor, Certification

MyUser = get_user_model()

__all__ = (
    'TutorRegisterSerializer',
)


class TutorRegisterSerializer(serializers.ModelSerializer):
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

    def update(self, instance, validated_data):
        print('update')
        instance.cert_type = validated_data.get('cert_type', instance.cert_type)
        instance.school = validated_data.get('school', instance.school)
        instance.major = validated_data.get('major', instance.major)
        instance.status_type = validated_data.get('status_type', instance.status_type)

        instance.save()
        return instance

    def validate_my_photo(self, data):
        return data

    def validate_nickname(self, data):
        return data

    def validate_phone(self, data):
        return data

    def validate_cert_name(self, data):
        return data

    def validate_cert_photo(self, data):
        return data

    def validate(self, data):
        return data
