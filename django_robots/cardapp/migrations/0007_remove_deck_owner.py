# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0006_deck_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='owner',
        ),
    ]
