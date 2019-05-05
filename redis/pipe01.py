#encoding=utf8

import redis


re = redis.Redis(host='192.168.178.115', port=6379)
#写
pipe=re.pipeline()
pipe.set('py10','hello01')
pipe.set('py11','hello02')
pipe.execute()

#读
print re.get('py10')