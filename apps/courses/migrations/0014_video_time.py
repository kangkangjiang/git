# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_courses_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='time',
            field=models.IntegerField(default=50, max_length=50, verbose_name='视频时长'),
        ),
    ]
