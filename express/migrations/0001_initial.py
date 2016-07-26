# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PublishTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq_no', models.CharField(max_length=13, verbose_name='\u53d1\u5e03\u5e8f\u5217\u53f7')),
                ('product', models.CharField(max_length=100, verbose_name='\u751f\u4ea7\u7ebf')),
                ('project', models.CharField(max_length=100, verbose_name='\u4ea7\u54c1\u540d\u79f0')),
                ('type', models.CharField(max_length=50, verbose_name='\u9879\u76ee\u7c7b\u578b')),
                ('version', models.CharField(max_length=50, verbose_name='\u7248\u672c')),
                ('update_remark', models.TextField(verbose_name='\u66f4\u65b0\u7406\u7531')),
                ('code_dir', models.TextField(verbose_name='\u4ee3\u7801\u5730\u5740')),
                ('settings', models.TextField(verbose_name='\u73af\u5883\u8bbe\u7f6e')),
                ('update_note', models.TextField(verbose_name='\u66f4\u65b0\u8bf4\u660e')),
                ('owner', models.CharField(max_length=100, verbose_name='\u9879\u76ee\u8d1f\u8d23\u4eba')),
                ('submit_time', models.DateTimeField(verbose_name='\u63d0\u4ea4\u65f6\u95f4')),
                ('submit_by', models.CharField(max_length=100, verbose_name='\u63d0\u4ea4\u4eba')),
                ('approval_time', models.DateTimeField(verbose_name='\u5ba1\u6838\u65f6\u95f4')),
                ('approval_by', models.CharField(max_length=100, verbose_name='\u5ba1\u6838\u4eba')),
                ('deploy_time', models.DateTimeField(verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('deploy_by', models.CharField(max_length=100, verbose_name='\u53d1\u5e03\u4eba')),
                ('status', models.CharField(max_length=100, verbose_name='\u72b6\u6001')),
            ],
        ),
    ]