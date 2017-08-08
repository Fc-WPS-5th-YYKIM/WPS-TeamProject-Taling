from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers, exceptions
from rest_framework.authtoken.models import Token
from django.utils.translation import ugettext_lazy as _
from rest_framework.response import Response

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
        print('update')
        print(validated_data)
        instance.username = validated_data.get('username', instance.username)
        # instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.my_photo = validated_data.get('my_photo', instance.my_photo)

        password = validated_data.get('password', None)
        instance.set_password(password)

        instance.save()
        return instance

    def validate(self, data):
        print('음?')
        if data['password'] and data['password'] != data['confirm_password']:
            raise serializers.ValidationError('비밀번호가 서로 일치하지 않습니다.')

        return data


class TalingLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=36, write_only=True)
    password = serializers.CharField(max_length=64, write_only=True)

    def validate(self, data):
        username = data['username']
        password = data['password']

        user = MyUser.objects.get(username=username)

        auth = authenticate(username=username, password=password)

        if auth == None:
            raise serializers.ValidationError({"detail": "Password is not matched"})

        token, created = user.get_user_token(user.pk)
        return token.key


class MyUserToken(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = (
            'key',
        )