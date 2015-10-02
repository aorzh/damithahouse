# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20151002_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryimage',
            name='category',
        ),
        migrations.AddField(
            model_name='gallery',
            name='category',
            field=models.ForeignKey(default=b'', blank=True, to='gallery.Category', null=True),
        ),
    ]
