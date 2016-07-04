# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 17:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=20)),
                ('time', models.DateTimeField(null=True)),
                ('is_finished', models.BigIntegerField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ExecLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('host', models.TextField()),
                ('cmd', models.TextField()),
                ('remote_ip', models.CharField(max_length=100)),
                ('result', models.TextField(default=b'')),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FileLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('host', models.TextField()),
                ('filename', models.TextField()),
                ('type', models.CharField(max_length=20)),
                ('remote_ip', models.CharField(max_length=100)),
                ('result', models.TextField(default=b'')),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, null=True)),
                ('host', models.CharField(max_length=200, null=True)),
                ('remote_ip', models.CharField(max_length=100)),
                ('login_type', models.CharField(max_length=100)),
                ('log_path', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField(null=True)),
                ('pid', models.IntegerField()),
                ('is_finished', models.BooleanField(default=False)),
                ('end_time', models.DateTimeField(null=True)),
                ('filename', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TermLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logPath', models.TextField()),
                ('filename', models.CharField(max_length=40)),
                ('logPWD', models.TextField()),
                ('nick', models.TextField(null=True)),
                ('log', models.TextField(null=True)),
                ('history', models.TextField(null=True)),
                ('timestamp', models.IntegerField(default=1465292623)),
                ('datetimestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TtyLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('cmd', models.CharField(max_length=200)),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jlog.Log')),
            ],
        ),
    ]
