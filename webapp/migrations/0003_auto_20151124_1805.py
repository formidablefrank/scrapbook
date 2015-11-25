# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20151124_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapbook',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='scrapbook',
            name='every',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='scrapbook',
            name='frequency',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='scrapbook',
            name='mode',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='scrapbook',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
