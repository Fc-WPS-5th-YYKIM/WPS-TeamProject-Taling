from django.contrib.auth import get_user_model
from django.db import models

from regiclass.models import Lecture

MyUser = get_user_model()


class Review(models.Model):
    lecture = models.ForeignKey(
        Lecture,
        related_name='reviews',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        MyUser,
    )
    curriculum_rate = models.CharField(
        max_length=1,
        default=0,
    )
    delivery_rate = models.CharField(
        max_length=1,
        default=0,
    )
    preparation_rate = models.CharField(
        max_length=1,
        default=0,
    )
    kindness_rate = models.CharField(
        max_length=1,
        default=0,
    )
    punctually_rate = models.CharField(
        max_length=1,
        default=0,
    )
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-modify_date']