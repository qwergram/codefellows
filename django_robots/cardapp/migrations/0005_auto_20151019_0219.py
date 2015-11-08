# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0004_auto_20151018_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='card',
            name='klass',
            field=models.CharField(choices=[('Water', 'Water'), ('Fire', 'Fire'), ('Wind', 'Wind'), ('Earth', 'Earth'), ('Light', 'Light'), ('Dark', 'Dark')], max_length=10),
        ),
        migrations.AddField(
            model_name='deck',
            name='cards',
            field=models.ManyToManyField(to='cardapp.Card'),
        ),
    ]
