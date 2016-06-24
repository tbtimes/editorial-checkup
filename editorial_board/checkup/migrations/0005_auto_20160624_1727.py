# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-24 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkup', '0004_auto_20160624_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respondent',
            name='gender',
            field=models.CharField(blank=True, choices=[(b'M', b'Male'), (b'F', b'Female')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='respondent',
            name='title',
            field=models.ForeignKey(blank=True, help_text=b"Displayed next to a person's name", null=True, on_delete=django.db.models.deletion.CASCADE, to='checkup.Title'),
        ),
    ]
