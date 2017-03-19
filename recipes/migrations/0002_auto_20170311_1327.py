# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='serves',
            field=models.PositiveIntegerField(default=1, help_text='# people this recipe serves'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='time',
            field=models.PositiveIntegerField(default=1, help_text='# minutes it takes to prepare the recipe'),
            preserve_default=False,
        ),
    ]
