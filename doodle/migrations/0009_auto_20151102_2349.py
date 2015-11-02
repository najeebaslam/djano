# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doodle', '0008_auto_20151031_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_date',
            field=models.DateTimeField(),
        ),
    ]
