# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-27 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albome', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
