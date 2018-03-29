# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-28 11:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attribution', '0019_auto_20180117_1324'),
    ]

    operations = [
        # Remove all deleted records physically
        migrations.RunSQL("DELETE FROM attribution_attribution CASCADE WHERE deleted is not null")
    ]
