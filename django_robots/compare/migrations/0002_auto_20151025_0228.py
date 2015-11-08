# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=1000)),
                ('klass', models.CharField(max_length=10, choices=[('Water', 'Water'), ('Fire', 'Fire'), ('Wind', 'Wind'), ('Earth', 'Earth'), ('Light', 'Light'), ('Dark', 'Dark')])),
                ('health', models.IntegerField(default=0)),
                ('water', models.IntegerField(default=0)),
                ('fire', models.IntegerField(default=0)),
                ('wind', models.IntegerField(default=0)),
                ('earth', models.IntegerField(default=0)),
                ('light', models.IntegerField(default=0)),
                ('dark', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AddField(
            model_name='card',
            name='image',
            field=models.OneToOneField(to='compare.Image', max_length=10),
        ),
    ]
