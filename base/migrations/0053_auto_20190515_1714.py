# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-05-15 15:14
from __future__ import unicode_literals

import base.models.learning_component_year
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0052_auto_20190424_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningcomponentyear',
            name='repartition_volume_additional_entity_1',
            field=base.models.learning_component_year.RepartitionVolumeField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='learningcomponentyear',
            name='repartition_volume_additional_entity_2',
            field=base.models.learning_component_year.RepartitionVolumeField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='learningcomponentyear',
            name='repartition_volume_requirement_entity',
            field=base.models.learning_component_year.RepartitionVolumeField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]