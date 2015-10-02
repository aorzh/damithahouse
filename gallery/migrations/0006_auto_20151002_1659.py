# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20151002_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='category',
            field=models.OneToOneField(to='gallery.Category'),
        ),
    ]
