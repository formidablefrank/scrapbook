# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('caption', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Scrapbook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('frequency', models.IntegerField(default=0)),
                ('every', models.IntegerField(default=0)),
                ('mode', models.IntegerField(default=0)),
                ('email', models.EmailField(blank=True, unique=True, max_length=50, null=True)),
            ],
        ),
    ]
