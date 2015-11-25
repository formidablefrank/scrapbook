# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='filename',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='picture',
            name='scrapbook',
            field=models.ForeignKey(default=1, to='webapp.Scrapbook'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scrapbook',
            name='email',
            field=models.EmailField(max_length=50, default=' ', blank=True),
            preserve_default=False,
        ),
    ]
