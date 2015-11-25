# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrapbook',
            name='email',
        ),
        migrations.RemoveField(
            model_name='scrapbook',
            name='every',
        ),
        migrations.RemoveField(
            model_name='scrapbook',
            name='frequency',
        ),
        migrations.RemoveField(
            model_name='scrapbook',
            name='mode',
        ),
        migrations.RemoveField(
            model_name='scrapbook',
            name='start_date',
        ),
    ]
