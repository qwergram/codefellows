# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cardapp', '0005_auto_20151019_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='owner',
            field=models.ForeignKey(default='nortonpengra', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
