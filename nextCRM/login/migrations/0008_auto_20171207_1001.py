# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-07 10:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_post_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='location',
        ),
        migrations.RemoveField(
            model_name='post',
            name='phone_number',
        ),
    ]
