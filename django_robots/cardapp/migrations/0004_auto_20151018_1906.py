# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0003_card_health'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='dark',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='card',
            name='light',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='card',
            name='earth',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='card',
            name='fire',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='card',
            name='health',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='card',
            name='water',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='card',
            name='wind',
            field=models.IntegerField(default=0),
        ),
    ]
