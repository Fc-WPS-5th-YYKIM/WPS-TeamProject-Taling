from django.conf import settings
from django.db import models

from member.models import MyUser


class Tutor(models.Model):
    CERT_TYPE_UNIV = 'univ'
    CERT_TYPE_GRAD = 'grad'
    CERT_TYPE_IDENTITY = 'identity'

    CERT_TYPE_CHOICE = (
        (CERT_TYPE_UNIV, '대학인증'),
        (CERT_TYPE_GRAD, '대학원인증'),
        (CERT_TYPE_IDENTITY, '신분증인증'),
    )

    STATUS_TYPE_CHOICE = (
        ('재학', '재학'),
        ('졸업', '졸업'),
        ('수료', '수료'),
    )

    author = models.OneToOneField(
        MyUser,
        related_name='myuser',
    )

    cert_type = models.CharField(
        max_length=1,
        choices=CERT_TYPE_CHOICE,
    )

    school = models.CharField(
        max_length=20,
        blank=True,
    )

    major = models.CharField(
        max_length=20,
        null=True,
    )

    status_type = models.CharField(
        max_length=1,
        choices=STATUS_TYPE_CHOICE,
        null=True,
    )

    identification = models.ImageField(
        upload_to='user/%Y/%m/%d',
        null=True,
    )

    ##
    # 앱에서 요구하는 필드
    ##

    # how_to_know = models.CharField(
    #     max_length=100,
    # )
    # age = models.CharField(
    #     max_length=3,
    # )
    # class_talent = models.CharField(
    #     max_length=20,
    #     null=True,
    # )
    # class_location = models.CharField(
    #     max_length=20,
    #     null=True,
    # )
