# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20151002_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='category',
            new_name='category_name',
        ),
        migrations.AddField(
            model_name='category',
            name='gallery_name',
            field=models.ManyToManyField(to='gallery.Gallery', blank=True),
        ),
    ]
