# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 09:26
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import member.models.myuser
import utils.fields.custom_image_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('my_photo', utils.fields.custom_image_fields.CustomImageField(blank=True, upload_to='user/%Y/%m/%d')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=13)),
                ('name', models.CharField(blank=True, max_length=12)),
                ('nickname', models.CharField(blank=True, max_length=24)),
                ('user_type', models.CharField(choices=[('d', 'Django'), ('f', 'Facebook')], default='d', max_length=1)),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            managers=[
                ('objects', member.models.myuser.MyUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cert_name', models.CharField(max_length=20, null=True)),
                ('cert_photo', models.ImageField(null=True, upload_to='user/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cert_type', models.CharField(choices=[('univ', '대학인증'), ('grad', '대학원인증'), ('identity', '신분증인증')], max_length=8)),
                ('school', models.CharField(blank=True, max_length=20)),
                ('major', models.CharField(max_length=20, null=True)),
                ('status_type', models.CharField(choices=[('ing', '재학'), ('graduation', '졸업'), ('complete', '수료')], max_length=10, null=True)),
                ('identification', models.ImageField(null=True, upload_to='user/%Y/%m/%d')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='myuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='certification',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Tutor'),
        ),
    ]
