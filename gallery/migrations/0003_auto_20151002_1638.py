# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20151002_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name=b'cropping',
            field=image_cropping.fields.ImageRatioField(b'image', '215x180', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping'),
        ),
    ]
