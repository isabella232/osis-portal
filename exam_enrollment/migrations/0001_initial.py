# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-02 07:41
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExamEnrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_id', models.CharField(max_length=10, unique=True)),
                ('offer_year_acronym', models.CharField(max_length=10, unique=True)),
                ('document', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
