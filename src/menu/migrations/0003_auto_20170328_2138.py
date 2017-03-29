# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import menu.models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menuweek_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuweek',
            name='image',
            field=models.ImageField(null=True, upload_to=menu.models.upload_location, blank=True),
        ),
    ]
