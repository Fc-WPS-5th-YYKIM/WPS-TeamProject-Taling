from django.db import models

from . import Lecture


class ClassLocation(models.model):
    CLASS_WEEKDAY_CHOICE = (
        (1, '월'),
        (2, '화'),
        (3, '수'),
        (4, '목'),
        (5, '금'),
        (6, '토'),
        (7, '일'),
    )

    lecture = models.ForeignKey(
        Lecture
    )
    location = models.CharField(
        max_length=20,
    )
    region_input = models.CharField(
        max_length=20,
    )
    region_price = models.CharField(
        max_length=10,
    )
    class_weekday = models.CharField(
        max_length=1,
        choices=CLASS_WEEKDAY_CHOICE,
    )
    class_time = models.CharField(
        max_length=10,
    )
