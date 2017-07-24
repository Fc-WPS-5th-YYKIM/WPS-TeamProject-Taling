from django.db import models
from . import MyUser


class Tutor(models.Model):
    CERT_TYPE_CHOICE = (
        (1, '대학인증'),
        (2, '대학원인증'),
        (3, '신분증인증'),
    )

    STATUS_TYPE_CHOICE = (
        (1, '재학'),
        (2, '졸업'),
        (3, '수료'),
    )

    author = models.OneToOneField(
        MyUser,
    )
    cert_type = models.CharField(
        max_length=1,
        choices=CERT_TYPE_CHOICE,
    )
    school_name = models.CharField(
        max_length=20,
        null=True,
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
    school_photo = models.ImageField(
        upload_to='user',
    )
    how_to_know = models.CharField(
        max_length=100,
    )
    age = models.CharField(
        max_length=3,
    )
    class_talent = models.CharField(
        max_length=20,
        null=True,
    )
    class_location = models.CharField(
        max_length=20,
        null=True,
    )
