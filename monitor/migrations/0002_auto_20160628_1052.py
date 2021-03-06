# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import opsplatform.until


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardGraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name=b'title')),
                ('hosts', models.CharField(max_length=100, verbose_name=b'hosts')),
                ('counters', models.CharField(max_length=100, verbose_name=b'counters')),
                ('screen_id', models.CharField(max_length=100, verbose_name=b'screen_id')),
                ('timespan', models.IntegerField(default=3600, verbose_name=b'timespan')),
                ('graph_type', models.CharField(default=b'h', max_length=10, verbose_name=b'graph_type')),
                ('method', models.CharField(max_length=100, verbose_name=b'method')),
                ('position', models.IntegerField(default=0, verbose_name=b'position')),
            ],
        ),
        migrations.CreateModel(
            name='DashboardScreen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', opsplatform.until.UnixTimestampField(auto_created=True, null=True)),
                ('pid', models.CharField(max_length=100, verbose_name=b'PID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='tmpgraph',
            name='ck',
            field=models.CharField(default=b'', max_length=32, verbose_name=b'ck'),
        ),
    ]
