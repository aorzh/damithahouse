# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0002_house_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseimage',
            name=b'cropping',
            field=image_cropping.fields.ImageRatioField(b'image', '215x180', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=True, adapt_rotation=False, help_text=None, verbose_name='cropping'),
        ),
    ]
