# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0011_auto_20170329_0137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='day',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='day',
        ),
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='products.Variation', through='carts.CartItem'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='item',
            field=models.ForeignKey(to='products.Variation'),
        ),
    ]
