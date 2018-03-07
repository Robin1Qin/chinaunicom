#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: dingyx 
@license: Apache Licence  
@contact: 1185867024@qq.com  18601720438
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: forms.py 
@time: 2018/1/11 13:51 
"""
from django.forms import ModelForm
from .models import XiaoQuGuZhang


class XiaoQuGuZhangForm(ModelForm):
    class Meta:
        model = XiaoQuGuZhang
        fields = ('account', 'bars')
        exclude = ['pub_date']
        error_messages = {
            'account': {
                'required': '不能为空'
            }
        }
