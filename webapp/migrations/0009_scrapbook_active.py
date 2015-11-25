# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20151125_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapbook',
            name='active',
            field=models.IntegerField(default=1),
        ),
    ]
