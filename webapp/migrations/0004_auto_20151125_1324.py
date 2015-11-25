# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20151124_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapbook',
            name='email',
            field=models.EmailField(max_length=50, blank=True, null=True),
        ),
    ]
