# -*- coding:utf-8 -*-

import redis
class RedisHelper():
    def __init__(self,host,port):
        self.__redis = redis.StrictRedis(host, port)
    def get(self,key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ""
    def set(self,key,value):
        self.__redis.set(key,value)