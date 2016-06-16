# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MRTapps', '0003_mrtstops_stop_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mrtstops',
            name='stop_color',
            field=models.CharField(choices=[('文湖線', '文湖線'), ('淡水信義線', '淡水信義線'), ('松山新店線', '松山新店線'), ('中和新蘆線', '中和新蘆線'), ('板南線', '板南線')], default='文湖線', max_length=10),
        ),
    ]
