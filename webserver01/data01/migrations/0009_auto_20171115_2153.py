# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data01', '0008_auto_20171115_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pd1_time',
            name='date',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='pd1_time',
            name='endtime',
            field=models.TimeField(default='12:00'),
        ),
        migrations.AlterField(
            model_name='pd1_time',
            name='starttime',
            field=models.TimeField(default='12:00'),
        ),
    ]