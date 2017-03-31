# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20170328_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuSelect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mo', models.CharField(max_length=100)),
                ('tu', models.CharField(max_length=100)),
                ('we', models.CharField(max_length=100)),
                ('th', models.CharField(max_length=100)),
                ('fr', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('day_max_pay', models.DateField(unique=True)),
                ('price', models.DecimalField(max_digits=20, decimal_places=2)),
                ('extra', models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('week', models.ForeignKey(to='menu.Menu')),
            ],
        ),
    ]
