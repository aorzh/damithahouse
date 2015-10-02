# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20151002_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('-title',),
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.RemoveField(
            model_name='galleryimage',
            name='title',
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='category',
            field=models.ForeignKey(default=b'', blank=True, to='gallery.Category', null=True),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name=b'cropping',
            field=image_cropping.fields.ImageRatioField(b'image', '215x180', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=True, adapt_rotation=False, help_text=None, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(upload_to=b'gallery', verbose_name=b'Image'),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='gallery',
            field=models.ForeignKey(default=b'', blank=True, to='gallery.Gallery', null=True),
        ),
    ]
