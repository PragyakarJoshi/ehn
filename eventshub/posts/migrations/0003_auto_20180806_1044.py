# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-06 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180806_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='closing_time',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='opening_time',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='registration',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
