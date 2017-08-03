from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers, exceptions
from rest_framework.authtoken.models import Token

MyUser = get_user_model()


class MyUserSerializer(serializers.ModelSerializer):
    # enrollments = serializers.PrimaryKeyRelatedField(many=True, read_only=True,)
    # user_token =

    class Meta:
        model = MyUser
        fields = (
            'id',
            'username',
            'email',
            'phone',

        )


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(label='Password', write_only=True)
    confirm_password = serializers.CharField(label='Confirm Password', write_only=True)

    class Meta:
        model = MyUser
        fields = (
            'username',
            'password',
            'confirm_password',
            'email',
            'phone',
            'my_photo',
        )

    def create(self, validated_data):
        return MyUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.my_photo = validated_data.get('my_photo', instance.photo)

        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and password == confirm_password:
            instance.set_password(password)

        instance.save()
        return instance

    def validate(self, data):
        if data['password'] and data['password'] != data['confirm_password']:
            raise serializers.ValidationError('비밀번호가 서로 일치하지 않습니다.')

        return data

# class TalingLoginSerializer(serializers.ModelSerializer):



class MyUserToken(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = (
            'key',
        )