# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapbook',
            name='email',
            field=models.EmailField(max_length=50, null=True, blank=True),
        ),
    ]
