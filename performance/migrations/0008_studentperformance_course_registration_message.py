# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-08-05 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0007_auto_20190313_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentperformance',
            name='course_registration_message',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
