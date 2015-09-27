# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='airbnb',
            field=models.URLField(verbose_name=b'Airbnb link', blank=True),
        ),
        migrations.AddField(
            model_name='room',
            name='bookingcom',
            field=models.URLField(verbose_name=b'Booking.com link', blank=True),
        ),
        migrations.AddField(
            model_name='room',
            name='tripsadvisor',
            field=models.URLField(verbose_name=b'Tripsadvisor link', blank=True),
        ),
    ]
