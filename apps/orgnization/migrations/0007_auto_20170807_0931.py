# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 09:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orgnization', '0006_auto_20170807_0815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orgcate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='机构类别·')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '机构类别',
                'verbose_name_plural': '机构类别',
            },
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='catgroy',
            field=models.ForeignKey(default='1', max_length=100, on_delete=django.db.models.deletion.CASCADE, to='orgnization.Orgcate'),
        ),
    ]
