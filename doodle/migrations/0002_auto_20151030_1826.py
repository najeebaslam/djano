# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doodle', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mdate',
            name='meeting',
        ),
        migrations.AddField(
            model_name='meeting',
            name='mdate',
            field=models.ForeignKey(default=None, to='doodle.Mdate'),
        ),
    ]
