# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_scrapbook_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
