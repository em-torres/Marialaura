# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fr1', models.ForeignKey(related_name='fr1', blank=True, to='products.Product', null=True)),
                ('fr2', models.ForeignKey(related_name='fr2', blank=True, to='products.Product', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuWeek',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('week', models.CharField(max_length=120, null=True, blank=True)),
                ('start_date', models.DateField(unique=True)),
                ('end_date', models.DateField(unique=True)),
                ('limit_pay', models.DateField(unique=True)),
                ('active', models.BooleanField(default=False)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_week',
            field=models.ForeignKey(related_name='menu_week', to='menu.MenuWeek'),
        ),
        migrations.AddField(
            model_name='menu',
            name='mo1',
            field=models.ForeignKey(related_name='mo1', blank=True, to='products.Product', null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='mo2',
            field=models.ForeignKey(related_name='mo2', blank=True, to='products.Product', null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='th1',
            field=models.ForeignKey(related_name='th1', blank=True, to='products.Product', null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='th2',
            field=models.ForeignKey(related_name='th2', blank=True, to='products.Product', null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='tu1',
            field=models.ForeignKey(related_name='tu1', blank=True, to='products.Product', null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='tu2',
            field=models.ForeignKey(related_name='tu2', blank=True, to='products.Product', null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='we1',
            field=models.ForeignKey(related_name='we1', blank=True, to='products.Product', null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='we2',
            field=models.ForeignKey(related_name='we2', blank=True, to='products.Product', null=True),
        ),
    ]
