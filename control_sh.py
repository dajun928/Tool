#!/usr/bin/python
# -*- coding: utf-8 -*-  
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import subprocess
import os
import shutil

#本类的方法
def push():
    print('Tick! The time is: %s' % datetime.now())
    cmd = 'sh auto_push_github.sh'
    subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

if __name__ == '__main__':
    push()
