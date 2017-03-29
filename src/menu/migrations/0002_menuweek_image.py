# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import menu.models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuweek',
            name='image',
            field=models.ImageField(height_field=b'height_field', width_field=b'width_field', null=True, upload_to=menu.models.upload_location, blank=True),
        ),
    ]
