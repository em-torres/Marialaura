# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0010_auto_20170326_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='products.Product', through='carts.CartItem'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='item',
            field=models.ForeignKey(to='products.Product'),
        ),
    ]
