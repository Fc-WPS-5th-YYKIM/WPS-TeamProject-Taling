from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class MyUser(AbstractUser):
    profile_photo = models.ImageField(
        upload_to='user',
        blank=True,
    )
    user_type = models.CharField(
        max_length=1,
        default='D',
    )
    # lecture_list = models.ManyToManyField(
    #     'Lecture',
    #     through='LectureList',
    # )
    # review_list = models.ManyToManyField(
    #     'Lecture',
    #     through='Review',
    # )
