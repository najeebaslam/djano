# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doodle', '0007_auto_20151030_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='meeting',
        ),
        migrations.AddField(
            model_name='meeting',
            name='room',
            field=models.ForeignKey(blank=True, to='doodle.Room', null=True),
        ),
    ]
