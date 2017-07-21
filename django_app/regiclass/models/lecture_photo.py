from django.db import models

from .lecture import Lecture


class LecturePhoto(models.Model):
    lecture = models.ForeignKey(
        Lecture,
    )
    photo_type = models.CharField(
        max_length=10,
        null=True,
    )
    photo = models.ImageField(
        upload_to='user',
        null=True,
    )
    description = models.CharField(
        max_length=20,
        null=True,
    )
