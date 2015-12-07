# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo1', '0004_auto_20151206_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='cat',
            new_name='catagory',
        ),
    ]
