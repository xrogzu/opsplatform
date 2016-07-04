# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-12 17:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='role',
            options={'permissions': (('perm_can_view_account', '\u7528\u6237\u6743\u9650\u7ba1\u7406'), ('perm_can_add_group', '\u65b0\u589e\u7528\u6237\u7ec4'), ('perm_can_change_group', '\u4fee\u6539\u7528\u6237\u7ec4'), ('perm_can_delete_group', '\u5220\u9664\u7528\u6237\u7ec4'), ('perm_can_view_group', '\u67e5\u770b\u7528\u6237\u7ec4'), ('perm_can_add_user', '\u65b0\u589e\u7528\u6237'), ('perm_can_change_user', '\u4fee\u6539\u7528\u6237'), ('perm_can_delete_user', '\u5220\u9664\u7528\u6237'), ('perm_can_view_user', '\u67e5\u770b\u7528\u6237'), ('perm_can_view_assets', '\u8d44\u4ea7\u7ba1\u7406'), ('perm_can_add_assetgroup', '\u65b0\u589e\u8d44\u4ea7\u7ec4'), ('perm_can_change_assetgroup', '\u4fee\u6539\u8d44\u4ea7\u7ec4'), ('perm_can_delete_assetgroup', '\u5220\u9664\u8d44\u4ea7\u7ec4'), ('perm_can_view_assetgroup', '\u67e5\u770b\u8d44\u4ea7\u7ec4'), ('perm_can_add_asset', '\u65b0\u589e\u8d44\u4ea7'), ('perm_can_change_asset', '\u4fee\u6539\u8d44\u4ea7'), ('perm_can_delete_asset', '\u5220\u9664\u8d44\u4ea7'), ('perm_can_view_asset', '\u67e5\u770b\u8d44\u4ea7'), ('perm_can_add_idc', '\u65b0\u589e\u673a\u623f'), ('perm_can_change_idc', '\u4fee\u6539\u673a\u623f'), ('perm_can_delete_idc', '\u5220\u9664\u673a\u623f'), ('perm_can_view_idc', '\u67e5\u770b\u673a\u623f'), ('perm_can_view_perm', '\u6388\u6743\u7ba1\u7406'), ('perm_can_add_permsudo', '\u65b0\u589eSudo'), ('perm_can_change_permsudo', '\u4fee\u6539Sudo'), ('perm_can_delete_permsudo', '\u5220\u9664Sudo'), ('perm_can_view_permsudo', '\u67e5\u770bSudo'), ('perm_can_add_permrole', '\u65b0\u589e\u7cfb\u7edf\u7528\u6237'), ('perm_can_change_permrole', '\u4fee\u6539\u7cfb\u7edf\u7528\u6237'), ('perm_can_delete_permrole', '\u5220\u9664\u7cfb\u7edf\u7528\u6237'), ('perm_can_view_permrole', '\u67e5\u770b\u7cfb\u7edf\u7528\u6237'), ('perm_can_add_permrule', '\u65b0\u589e\u6388\u6743\u89c4\u5219'), ('perm_can_change_permrule', '\u4fee\u6539\u6388\u6743\u89c4\u5219'), ('perm_can_delete_permrule', '\u5220\u9664\u6388\u6743\u89c4\u5219'), ('perm_can_view_permrule', '\u67e5\u770b\u6388\u6743\u89c4\u5219'), ('perm_can_conn_asset', 'SSH\u8fde\u63a5\u8d44\u4ea7'), ('perm_can_exec_cmd', '\u6267\u884c\u6279\u91cf\u547d\u4ee4'), ('perm_can_role_push', '\u63a8\u9001\u7cfb\u7edf\u7528\u6237'), ('perm_can_view_log', '\u67e5\u770b\u65e5\u5fd7\u4fe1\u606f'), ('perm_can_upload_download_file', '\u4e0a\u4f20\u4e0b\u8f7d\u6587\u4ef6'), ('perm_can_view_dashboard', '\u67e5\u770b\u7edf\u8ba1\u65e5\u5fd7'))},
        ),
    ]
