from django.db import models

from regiclass.models import Lecture


class LecturePhoto(models.Model):
    PHOTO_TYPE_INFO = 'info'
    PHOTO_TYPE_CURRICULUM = 'curriculum'

    PHOTO_TYPE_CHOICE = (
        (PHOTO_TYPE_INFO, ''),
        (PHOTO_TYPE_CURRICULUM, '')
    )
    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.CASCADE
    )
    photo_type = models.CharField(
        max_length=10,
        choices=PHOTO_TYPE_CHOICE,
    )
    photo = models.ImageField(
        upload_to='class/images/%Y/%m/%d',
    )
    description = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['photo_type']