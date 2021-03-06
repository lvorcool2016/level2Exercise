# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-30 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(blank=True, max_length=500, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('tag', models.CharField(blank=True, choices=[('tech', 'Tech'), ('life', 'Life')], max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('job', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
