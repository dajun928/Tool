#encoding=utf8

import redis

class Task(object):
    def __init__(self):
        self.rcon = redis.StrictRedis(host='192.168.178.115', port=6379)
        # self.queue = 'task:prodcons:queue'
        self.queue = 'wlt-spider'
        # self.queue =['spider-H','spider-L']

    def listen_task(self):
        while True:
            task = self.rcon.blpop(self.queue)[1]
            print "Task get", task

if __name__ == '__main__':
    print 'listen task queue'
    Task().listen_task()

