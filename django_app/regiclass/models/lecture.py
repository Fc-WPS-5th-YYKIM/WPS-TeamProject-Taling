from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

MyUser = get_user_model()

__all__ = (
    'Lecture',
    'LikeLecture',
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

    STATE_EDITING = 'editing'
    STATE_ACTIVITY = 'activity'

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

    STATE_CHOICE = (
        (STATE_EDITING, '작성중'),
        (STATE_ACTIVITY, '활동중'),
    )

    tutor = models.ForeignKey(
        'member.Tutor',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=30,
    )
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICE,
    )
    class_type = models.CharField(
        max_length=10,
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
        max_length=10,
    )
    total_count = models.CharField(
        max_length=10,
    )
    youtube_url1 = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    youtube_url2 = models.CharField(
        max_length=100,
        blank=True,
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
    state = models.CharField(
        max_length=10,
        choices=STATE_CHOICE,
        default=STATE_EDITING,
    )
    like_users = models.ManyToManyField(
        MyUser,
        related_name='like_lecture',
        through='LikeLecture',
    )
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)


class LikeLecture(models.Model):
    user = models.ForeignKey(MyUser)
    lecture = models.ForeignKey(Lecture)


class Enrollment(models.Model):
    class Meta:
        unique_together = (
            ('user', 'lecture'),
        )

    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
    )
    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.CASCADE,
    )
    create_date = models.DateTimeField(auto_now_add=True)

    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.CASCADE,
        related_name='enrollment_lecture',
    )

    location = models.CharField(
        max_length=12,
        blank=True,
    )

    time = models.CharField(
        max_length=48,
        blank=True,
    )

    LEVEL_BEGINNER = 'beginner'
    LEVEL_INTERMEDIATE = 'intermediate'
    LEVEL_ADVANCED = 'advanced'

    LEVEL_CHOICE = (
        (LEVEL_BEGINNER, '입문자'),
        (LEVEL_INTERMEDIATE, '초중급자'),
        (LEVEL_ADVANCED, '상급자'),
    )

    level = models.CharField(
        max_length=12,
        choices=LEVEL_CHOICE,
        blank=True,
    )

    career = models.CharField(max_length=36, blank=True,)
    to_tutor = models.TextField(blank=True,)
    created_at = models.DateTimeField(auto_now_add=True,)
    modified_at = models.DateTimeField(auto_now=True,)

    PAY_METHOD_CREDIT = 'credit'
    PAY_METHOD_BANKBOOK = 'bankbook'

    PAY_METHOD_CHOICE = (
        (PAY_METHOD_CREDIT, '신용카드'),
        (PAY_METHOD_BANKBOOK, '무통장입금'),
    )

    pay_method = models.CharField(
        max_length=12,
        choices=PAY_METHOD_CHOICE,
        blank=True,
    )

    remitter = models.CharField(
        max_length=24,
        blank=True,
    )

    due_date = models.DateTimeField(blank=True,)
