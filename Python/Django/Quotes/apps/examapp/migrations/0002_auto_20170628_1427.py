# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 18:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='quote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='examapp.Quote'),
        ),
    ]