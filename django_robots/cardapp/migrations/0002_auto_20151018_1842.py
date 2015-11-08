# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='card_desc',
            field=models.CharField(max_length=1000, default='n/a'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='card_name',
            field=models.CharField(max_length=200, default='A Card'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='img',
            field=models.CharField(max_length=200, default='http://www.flickeringmyth.com/wp-content/uploads/2014/09/destiny-25788-1920x1080.jpg'),
            preserve_default=False,
        ),
    ]
