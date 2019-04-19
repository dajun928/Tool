#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@version : 2.7.14
@file : auto_shutdown.py
@time : 2019/03/04 23:43:07
@func : 工具脚本-定时关机
"""
import sys
import os
import time

reload(sys)
sys.setdefaultencoding("GBK")

# shutdown computer after time_diff seconds
def shutdown(seconds):
    print str(seconds) + u' 秒后将会关机...'
    time.sleep(seconds)
    print u'关机啦。。。'
    # os.system('shutdown -s -f -t 1')

def main():
    hour = input(u'延迟关机小时数：')
    print hour
    shutdown(hour * 3600)

if __name__ == '__main__':
    main()
