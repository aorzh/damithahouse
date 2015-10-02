# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=b'houses', verbose_name=b'Image')),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '215x180', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=True, adapt_rotation=False, help_text=None, verbose_name='cropping')),
                ('category', models.ForeignKey(to='gallery.Category')),
            ],
            options={
                'ordering': ('-image',),
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
