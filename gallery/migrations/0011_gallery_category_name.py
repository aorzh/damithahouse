# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_remove_gallery_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='category_name',
            field=models.ForeignKey(default=b'', blank=True, to='gallery.Category', null=True),
        ),
    ]
