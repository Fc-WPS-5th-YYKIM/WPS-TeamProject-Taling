from django.conf import settings
from django.db import models

__all__ = (
    'Lecture',
    'Enrollment'
)


class Lecture(models.Model):
    CATEGORY_HEALTHNBEAUTY = 'hbn'
    CATEGORY_LANG = 'lang'
    CATEGORY_COMPUTER = 'com'
    CATEGORY_MUSICNART = 'mna'
    CATEGORY_SPORTS = 'sports'
    CATEGORY_MAJOR = 'major'
    CATEGORY_HOBBY = 'hobby'

    CLASS_TYPE_ONETOONE = 'onetoone'
    CLASS_TYPE_GROUP = 'group'
    CLASS_TYPE_ONEDAY = 'oneday'

    CATEGORY_CHOICE = (
        (CATEGORY_HEALTHNBEAUTY, '헬스&뷰티'),
        (CATEGORY_LANG, '외국어'),
        (CATEGORY_COMPUTER, '컴퓨터'),
        (CATEGORY_MUSICNART, '음악 / 미술'),
        (CATEGORY_SPORTS, '스포츠'),
        (CATEGORY_MAJOR, '전공 / 취업'),
        (CATEGORY_HOBBY, '이색취미'),
    )
    CLASS_TYPE_CHOICE = (
        (CLASS_TYPE_ONETOONE, '1:1수업'),
        (CLASS_TYPE_GROUP, '그룹수업'),
        (CLASS_TYPE_ONEDAY, '원데이')
    )
    MEMBER_COUNT = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
    )

    tutor = models.ForeignKey(
        'member.Tutor',
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
        upload_to='class/cover/%Y/%m/%d',
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
