# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('regiclass', '0001_initial'),
        ('member', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
        ('authtoken', '0002_auto_20160226_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='enrollments',
            field=models.ManyToManyField(related_name='enroll_lectures', through='regiclass.Enrollment', to='regiclass.Lecture'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_token',
            field=models.ManyToManyField(to='authtoken.Token'),
        ),
    ]
