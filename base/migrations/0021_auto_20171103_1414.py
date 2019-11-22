# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-03 13:14
from __future__ import unicode_literals

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_auto_20171102_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearningContainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('external_id', models.CharField(blank=True, max_length=100, null=True)),
                ('changed', models.DateTimeField(auto_now=True, null=True)),
                ('auto_renewal_until', models.IntegerField(null=True)),
                ('start_year', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='learningcontaineryear',
            name='learning_container',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.LearningContainer'),
        ),
    ]
