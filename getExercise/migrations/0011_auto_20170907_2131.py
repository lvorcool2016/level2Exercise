# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-07 21:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('getExercise', '0010_comment_createdon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='createdOn',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
