# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-23 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopify_sync', '0016_null_variant_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='variant_title',
            field=models.CharField(max_length=256, null=True),
        ),
    ]