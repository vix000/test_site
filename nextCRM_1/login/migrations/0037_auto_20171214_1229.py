# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-14 12:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0036_auto_20171214_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companycomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]