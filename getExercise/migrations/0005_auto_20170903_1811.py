# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-03 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getExercise', '0004_auto_20170903_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='文章附图'),
        ),
    ]
