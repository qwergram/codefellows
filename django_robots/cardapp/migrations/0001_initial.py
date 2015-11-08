# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('water', models.IntegerField()),
                ('fire', models.IntegerField()),
                ('wind', models.IntegerField()),
                ('earth', models.IntegerField()),
                ('klass', models.CharField(choices=[('Wa', 'Water'), ('Fi', 'Fire'), ('Wi', 'Wind'), ('Ea', 'Earth'), ('Li', 'Light'), ('Da', 'Dark')], max_length=2)),
            ],
        ),
    ]
