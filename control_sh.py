#!/usr/bin/python
# -*- coding: utf-8 -*-  
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import subprocess
import os
import shutil
import time
import random

def push():
    num = random.randint(1, 6)
    for i in range(num):
        cmd = 'sh auto_push_github.sh'
        subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        time.sleep(10)

if __name__ == '__main__':
    scheduler = BlockingScheduler()

    scheduler.add_job(push, 'cron', hour ='0',minute ='2')

    # 启动调度
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

