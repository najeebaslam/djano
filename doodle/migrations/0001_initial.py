# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('choice_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mdate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mdate', models.DateTimeField(auto_now_add=True, verbose_name=b'meeting date')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('r_votes', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=200)),
                ('capasity', models.IntegerField(default=10)),
                ('meeting', models.ForeignKey(to='doodle.Meeting')),
            ],
        ),
        migrations.AddField(
            model_name='mdate',
            name='meeting',
            field=models.ForeignKey(to='doodle.Meeting'),
        ),
        migrations.AddField(
            model_name='choice',
            name='meeting',
            field=models.ForeignKey(to='doodle.Meeting'),
        ),
    ]
