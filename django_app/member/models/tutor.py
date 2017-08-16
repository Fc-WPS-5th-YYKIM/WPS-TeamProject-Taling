from django.contrib.auth import get_user_model
from django.db import models

from django.db.models import permalink
from django.db.models.signals import pre_save
from django.utils.text import slugify
from rest_framework.reverse import reverse

from unidecode import unidecode

MyUser = get_user_model()


class Tutor(models.Model):
    CERT_TYPE_UNIV = 'univ'
    CERT_TYPE_GRAD = 'grad'
    CERT_TYPE_IDENTITY = 'identity'

    CERT_TYPE_CHOICE = (
        (CERT_TYPE_UNIV, '대학인증'),
        (CERT_TYPE_GRAD, '대학원인증'),
        (CERT_TYPE_IDENTITY, '신분증인증'),
    )

    STATUS_TYPE_ING = 'ing'
    STATUS_TYPE_GRADUATION = 'graduation'
    STATUS_TYPE_COMPLETE = 'complete'
    STATUS_TYPE_CHOICE = (
        ('ing', '재학'),
        ('graduation', '졸업'),
        ('complete', '수료'),
    )

    author = models.OneToOneField(
        MyUser,
        related_name='myuser',
    )

    cert_type = models.CharField(
        max_length=8,
        choices=CERT_TYPE_CHOICE,
    )

    school = models.CharField(
        max_length=20,
        blank=True,
    )

    major = models.CharField(
        max_length=20,
        null=True,
    )

    status_type = models.CharField(
        max_length=10,
        choices=STATUS_TYPE_CHOICE,
        null=True,
    )

    identification = models.ImageField(
        upload_to='user/%Y/%m/%d',
        null=True,
    )

    ##
    # 슬러그 생성
    ##
    slug = models.SlugField(
        unique=True,
        blank=True,
        db_index=True,
        allow_unicode=True,
    )

    # @permalink
    # def get_absolute_url(self):
    #     return reverse("member:detail", (), {
    #       'pk': self.pk,
    #       'slug': self.slug,
    #     })


def create_slug(instance, new_slug=None):
    slug = slugify('tutor-' + unidecode(instance.author.nickname))
    if new_slug is not None:
        slug = new_slug
    qs = Tutor.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = '{}-{}'.format(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Tutor)

    ##
    # 앱에서 요구하는 필드
    ##

    # how_to_know = models.CharField(
    #     max_length=100,
    # )
    # age = models.CharField(
    #     max_length=3,
    # )
    # class_talent = models.CharField(
    #     max_length=20,
    #     null=True,
    # )
    # class_location = models.CharField(
    #     max_length=20,
    #     null=True,
    # )