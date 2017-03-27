# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0009_cart_tax_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='day',
            field=models.CharField(default='mo', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='day',
            field=models.CharField(default='mo', max_length=20),
            preserve_default=False,
        ),
    ]
