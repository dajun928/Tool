#encoding=utf8

#不断地向redis里面拉取任务参数
import time
import redis
# 连接Linux服务器上的redis

re = redis.Redis(host='192.168.178.115', port=6379)


def start01():
    for i in range(100):
        # time.sleep(1)
        print i
        re.lpush('spider-H', '%s' % 'spider-H'+str(i))


def start02():
    for i in range(50):
        # time.sleep(1)
        print i
        re.lpush('spider-L', '%s' % 'spider-L'+str(i))


start01()
start02()




















