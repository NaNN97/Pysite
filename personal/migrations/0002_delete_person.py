# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-18 17:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
