# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-02 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0006_auto_20170302_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internshipstudentinformation',
            name='contest',
            field=models.CharField(choices=[('SP', 'SP'), ('SS', 'SS')], default='GENERALIST', max_length=124),
        ),
    ]
