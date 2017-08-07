from django.db import models
from . import Tutor


class Certification(models.Model):
    tutor = models.ForeignKey(Tutor)
    # 자격증
    cert_name = models.CharField(max_length=20, null=True)
    # 자격증 이미지
    cert_photo = models.ImageField(upload_to='user/%Y/%m/%d', null=True)
