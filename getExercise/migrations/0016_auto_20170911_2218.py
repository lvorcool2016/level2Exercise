# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-11 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getExercise', '0015_auto_20170911_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='avatar',
            field=models.CharField(default='http://n.sinaimg.cn/ent/crawl/20170907/K0wM-fykufii0195474.jpg', max_length=500),
        ),
    ]
