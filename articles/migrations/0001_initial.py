# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('body', ckeditor.fields.RichTextField()),
                ('time', models.DateField()),
            ],
            options={
                'ordering': ('-title', 'time'),
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
