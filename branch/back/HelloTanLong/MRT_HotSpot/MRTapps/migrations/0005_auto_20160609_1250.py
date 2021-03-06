# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MRTapps', '0004_auto_20160609_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='MRTLines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='mrtstops',
            name='stop_color',
        ),
        migrations.AddField(
            model_name='mrtstops',
            name='stop_line',
            field=models.ManyToManyField(to='MRTapps.MRTLines'),
        ),
    ]
