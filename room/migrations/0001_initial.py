# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('airbnb', models.URLField(verbose_name=b'Airbnb link', blank=True)),
                ('bookingcom', models.URLField(verbose_name=b'Booking.com link', blank=True)),
                ('tripsadvisor', models.URLField(verbose_name=b'Tripsadvisor link', blank=True)),
                ('house_have_room', models.ForeignKey(default=b'', blank=True, to='house.House', null=True)),
            ],
            options={
                'ordering': ('-title',),
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'houses', verbose_name=b'Image')),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '215x180', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping')),
                ('obj', models.ForeignKey(to='room.Room')),
            ],
            options={
                'ordering': ('-image',),
                'verbose_name': 'Room image',
                'verbose_name_plural': 'Room images',
            },
        ),
    ]
