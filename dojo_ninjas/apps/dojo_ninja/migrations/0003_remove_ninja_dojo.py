# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-15 03:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninja', '0002_auto_20170815_0233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ninja',
            name='dojo',
        ),
    ]