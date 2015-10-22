# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sliderimage',
            options={'ordering': ('-image',), 'verbose_name': 'Slider image', 'verbose_name_plural': 'Slider images'},
        ),
    ]
