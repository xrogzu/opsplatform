# encoding: utf-8

"""
@version: 
@author: liriqiang
@file: forms.py
@time: 16-6-7 下午1:23
"""
from django import forms

from asset.models import IDC, Asset, AssetGroup


class AssetForm(forms.ModelForm):

    class Meta:
        model = Asset

        fields = [
            "ip", "other_ip", "hostname", "port", "group", "username", "password", "use_default_auth",
            "idc", "mac", "remote_ip", "brand", "cpu", "memory", "disk", "system_type", "system_version",
            "cabinet", "position", "number", "status", "asset_type", "env", "sn", "is_active", "comment",
            "system_arch"
        ]


class AssetGroupForm(forms.ModelForm):
    class Meta:
        model = AssetGroup
        fields = [
            "name", "comment"
        ]


class IdcForm(forms.ModelForm):
    class Meta:
        model = IDC
        fields = ['name', "bandwidth", "operator", 'linkman', 'phone', 'address', 'network', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'network': forms.Textarea(
                attrs={'placeholder': '192.168.1.0/24\n192.168.2.0/24'})
        }


