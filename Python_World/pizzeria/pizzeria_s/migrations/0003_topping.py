# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 04:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria_s', '0002_auto_20170605_0359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('Pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzeria_s.Pizza')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]