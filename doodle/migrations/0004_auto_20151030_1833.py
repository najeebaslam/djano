# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doodle', '0003_auto_20151030_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='mdate',
            field=models.ForeignKey(default=None, blank=True, to='doodle.Mdate'),
        ),
    ]
