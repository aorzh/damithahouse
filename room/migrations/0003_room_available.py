# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_auto_20151002_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='available',
            field=models.BooleanField(default=False, verbose_name=b'Room is closed'),
        ),
    ]
