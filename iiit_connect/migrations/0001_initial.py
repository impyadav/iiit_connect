# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailInvitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.EmailField(max_length=70)),
                ('To', models.EmailField(max_length=70)),
                ('Subject', models.CharField(max_length=200)),
                ('uniqueCode', models.IntegerField()),
                ('eventName', models.CharField(max_length=100)),
            ],
        ),
    ]
