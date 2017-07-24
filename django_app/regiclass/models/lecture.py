# 클래스 등록 정보
# Step1 ~ 4 까지의 데이터는 Update 가 아닌 Insert로 구현
# Update 보다 Insert의 연산 속도가 더 빠름
from django.db import models
from member.models import Tutor, MyUser


class Lecture(models.Model):
    CATEGORY_CHOICE = (
        (1, '헬스&뷰티'),
        (2, '외국어'),
        (3, '컴퓨터'),
        (4, '음악 / 미술'),
        (5, '스포츠'),
        (6, '전공 / 취업'),
        (7, '이색취미'),
    )
    CLASS_TYPE_CHOICE = (
        (1, '1:1수업'),
        (2, '그룹수업'),
        (3, '원데이')
    )
    MEMBER_COUNT = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
    )

    tutor = models.ForeignKey(
        Tutor,
    )
    title = models.CharField(
        max_length=30,
    )
    category = models.CharField(
        max_length=1,
        choices=CATEGORY_CHOICE,
    )
    class_type = models.CharField(
        max_length=1,
        choices=CLASS_TYPE_CHOICE,
    )
    min_member = models.CharField(
        max_length=1,
        null=True,
        choices=MEMBER_COUNT,
    )
    max_member = models.CharField(
        max_length=1,
        null=True,
        choices=MEMBER_COUNT,
    )
    cover_photo = models.ImageField(
        upload_to='user',
    )
    tutor_intro = models.CharField(
        max_length=100,
    )
    class_intro = models.CharField(
        max_length=100,
    )
    target_intro = models.CharField(
        max_length=100,
    )
    price = models.CharField(
        max_length=10,
    )
    basic_class_time = models.CharField(
        max_length=1,
    )
    total_count = models.CharField(
        max_length=1,
    )
    youtube_url1 = models.CharField(
        max_length=100,
        null=True,
    )
    youtube_url2 = models.CharField(
        max_length=100,
        null=True,
    )
    region_comment = models.CharField(
        max_length=100,
        null=True,
    )
    notice = models.CharField(
        max_length=100,
        null=True,
    )
