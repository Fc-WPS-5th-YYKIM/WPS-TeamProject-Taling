# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 10:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regiclass', '0004_auto_20170824_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor_info', to=settings.AUTH_USER_MODEL),
        ),
    ]