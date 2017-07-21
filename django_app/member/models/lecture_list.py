from django.db import models

from member.models import MyUser
from regiclass.models import Lecture


class LectureList(models.Model):
    WEEKDAY_CHOICE = (
        (1, '월'),
        (2, '화'),
        (3, '수'),
        (4, '목'),
        (5, '금'),
        (6, '토'),
        (7, '일'),
    )
    myuser = models.ForeignKey(
        MyUser,
    )
    lecture = models.ForeignKey(
        Lecture,
    )
    location = models.CharField(
        max_length=20,
    )
    weekday = models.CharField(
        max_length=1,
        choices=WEEKDAY_CHOICE,
    )
    time = models.CharField(
        max_length=10,
    )
    level = models.CharField(
        max_length=10,
    )
    career = models.CharField(
        max_length=10,
    )
    to_tutor = models.CharField(
        max_length=30,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
