# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='ABC', unique=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='Started', choices=[('Started', 'Started'), ('Abandoned', 'Abandoned'), ('Finished', 'Finished')], max_length=120),
        ),
    ]
