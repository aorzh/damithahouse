# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_auto_20151002_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='category_name',
            field=models.ForeignKey(default=b'', blank=True, to='gallery.Category', null=True),
        ),
    ]
