# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20151125_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='pic',
            field=models.ImageField(default='assets/no-img.jpg', upload_to='assets/scrapbooks/'),
        ),
    ]
