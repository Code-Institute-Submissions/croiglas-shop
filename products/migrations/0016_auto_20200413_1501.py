# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-13 15:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20200413_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainfilter',
            name='person_category',
        ),
        migrations.AddField(
            model_name='mainfilter',
            name='pers_category',
            field=models.CharField(choices=[('M', 'Men'), ('W', 'Women'), ('K', 'Kids')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='person_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.MainFilter'),
        ),
    ]
