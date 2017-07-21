from django.db import models

from member.models import Tutor, MyUser


class Review(models.Model):
    lecture = models.ForeignKey(
        Tutor,
    )
    author = models.ForeignKey(
        MyUser,
    )
    curriculum_rate = models.IntegerField(
        max_length=10,
        default=0,
    )
    delivery_rate = models.IntegerField(
        max_length=10,
        default=0,
    )
    preparation_rate = models.IntegerField(
        max_length=10,
        default=0,
    )
    kindness_rate = models.IntegerField(
        max_length=10,
        default=0,
    )
    punctually_rate = models.IntegerField(
        max_length=10,
        default=0,
    )
    content = models.CharField(
        max_length=100,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    modify_at = models.DateTimeField(
        auto_now=True,
    )
