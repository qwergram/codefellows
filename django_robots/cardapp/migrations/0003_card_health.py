# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0002_auto_20151018_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='health',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
