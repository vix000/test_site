# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-11 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0028_auto_20171209_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]