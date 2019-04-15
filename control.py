#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : control.py
@time : 2019/04/16 00:09:31
@func : 
"""
import subprocess

cmd = 'sh push_test02.sh control.py'
a = subprocess.getstatusoutput(cmd)
