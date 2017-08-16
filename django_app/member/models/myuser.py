from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager
from django.db import models

from utils import CustomImageField

from rest_framework.authtoken.models import Token

__all__ = (
    'MyUser'
)


class MyUserManager(DefaultUserManager):
    def get_or_create_facebook_user(self, user_info):
        username = '{}_{}_{}'.format(
            self.model.USER_TYPE_FACEBOOK,
            settings.FACEBOOK_APP_ID,
            user_info['id'],
        )
        user, user_created = self.get_or_create(
            username=username,
            email=user_info.get('email'),
            user_type=self.model.USER_TYPE_FACEBOOK,
            defaults={
                'email': user_info.get('email', ''),
                'my_photo': user_info['picture']['data'].get('url', '뭥미'),
            }
        )
        return user


class MyUser(AbstractUser):
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
    name = models.CharField(
        max_length=12,
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
        'regiclass.Lecture',
        through='Enrollment',
        related_name='enroll_lectures',
    )

    nickname = models.CharField(
        max_length=24,
        null=True,
        blank=True,
        unique=True,
    )

    user_token = models.ManyToManyField(Token)

    objects = MyUserManager()

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='my_profile', null=True)

    def info_update(self, **kwargs):
        self.my_photo = kwargs.get('my_photo', '')
        self.nickname = kwargs['nickname']
        self.phone = kwargs['phone']
        self.save()

    def get_user_token(self, user_pk):
        return Token.objects.get_or_create(user_id=user_pk)


class Enrollment(models.Model):
    ##
    # 로그인한 모든 회원에게만 수강 등록 권한이 있다.
    ##
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='enrollment_user',
    )

    lecture = models.ForeignKey('regiclass.Lecture')
