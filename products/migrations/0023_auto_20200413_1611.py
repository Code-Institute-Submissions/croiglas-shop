# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-13 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20200413_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
