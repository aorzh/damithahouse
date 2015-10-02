# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_auto_20151002_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='category_name',
        ),
    ]
