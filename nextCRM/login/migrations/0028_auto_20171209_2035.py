# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 19:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0027_remove_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post_id',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]