# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='sales',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='products/images/'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='category',
            field=models.CharField(max_length=120),
        ),
    ]
