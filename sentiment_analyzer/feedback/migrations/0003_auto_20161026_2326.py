# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 23:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20161026_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='actual_sentiment',
            field=models.CharField(blank=True, choices=[('', '---'), ('positive', 'positive'), ('neutral', 'neutral'), ('negative', 'negative')], default='', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='predicted_sentiment',
            field=models.CharField(blank=True, choices=[('', '---'), ('positive', 'positive'), ('neutral', 'neutral'), ('negative', 'negative')], default='', max_length=8, null=True),
        ),
    ]
