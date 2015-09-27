# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('house_have_room', models.ForeignKey(default=b'', blank=True, to='house.House', null=True)),
            ],
            options={
                'ordering': ('-title',),
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
        ),
    ]
