#-*- coding: UTF-8 -*-



from  testredis01 import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
    msg = redis_sub.parse_response()
    print(u'接收：',msg)