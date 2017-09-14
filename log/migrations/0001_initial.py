# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('date', models.DateField(max_length=50)),
                ('description', models.CharField(max_length=400)),
                ('time', models.TimeField(max_length=50)),
            ],
        ),
    ]