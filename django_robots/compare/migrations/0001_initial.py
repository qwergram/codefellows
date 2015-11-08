# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('image_desc', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(verbose_name='date uploaded')),
                ('image', models.ImageField(upload_to='user_content')),
                ('wins', models.IntegerField()),
                ('loses', models.IntegerField()),
            ],
        ),
    ]
