# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20151125_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='filename',
        ),
        migrations.AddField(
            model_name='picture',
            name='pic',
            field=models.ImageField(default='pic_folder/none/no-img.jpg', upload_to='folder/'),
        ),
    ]
