# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-11 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0029_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='profile_image'),
        ),
    ]
