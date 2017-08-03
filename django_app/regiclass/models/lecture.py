from django.conf import settings
from django.db import models


class Lecture(models.Model):
    pass


class Enrollment(models.Model):
    ##
    # 로그인한 모든 회원에게만 수강 등록 권한이 있다.
    ##
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='enrollment_user',
    )

    lecture = models.ForeignKey(Lecture)