from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager
from django.db import models

from regiclass.models import Lecture, Enrollment
from utils import CustomImageField

from rest_framework.authtoken.models import Token

__all__ = (
    'MyUser'
)


class MyUserManager(DefaultUserManager):
    def get_or_create_facebook_user(self, user_info):
        print(user_info)
        username = '{}_{}_{}'.format(
            self.model.USER_TYPE_FACEBOOK,
            settings.FACEBOOK_APP_ID,
            user_info['id'],
        )
        print(username)
        user, user_created = self.get_or_create(
            username=username,
            email=user_info.get('email'),
            user_type=self.model.USER_TYPE_FACEBOOK,
            defaults={
                'email': user_info.get('email', ''),
            }
        )
        return user


class MyUser(AbstractUser):
    confirm_password = models.CharField(
        max_length=64,
        blank=True,
    )
    my_photo = CustomImageField(
        upload_to='user/%Y/%m/%d',
        blank=True,
    )
    email = models.EmailField(
        blank=True,
    )
    phone = models.CharField(
        max_length=13,
        blank=True,
    )

    ##
    # 유저타입. 기본은 Django, 페이스북 로그인 시 USER_TYPE_FACEBOOK 값을 갖는다.
    ##
    USER_TYPE_DJANGO = 'd'
    USER_TYPE_FACEBOOK = 'f'
    USER_TYPE_CHOICES = (
        (USER_TYPE_DJANGO, 'Django'),
        (USER_TYPE_FACEBOOK, 'Facebook'),
    )
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default=USER_TYPE_DJANGO)

    enrollments = models.ManyToManyField(
        Lecture,
        through=Enrollment,
        related_name='enroll_lectures',
    )

    nickname = models.CharField(max_length=20, null=True, blank=True)

    user_token = models.ManyToManyField(Token)

    objects = MyUserManager()

    def info_update(self, **kwargs):
        self.my_photo = kwargs.get('my_photo', '')
        self.nickname = kwargs['nickname']
        self.phone = kwargs['phone']
        self.save()

    def get_user_token(self, user_pk):
        return Token.objects.get_or_create(user_id=user_pk)
