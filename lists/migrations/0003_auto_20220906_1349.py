# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-09-06 13:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20220906_1223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='lists',
            new_name='list',
        ),
    ]
