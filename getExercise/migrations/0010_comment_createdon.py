# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-07 21:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('getExercise', '0009_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='createdOn',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
    ]
