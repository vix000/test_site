# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 19:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0026_companycomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]