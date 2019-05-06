#encoding=utf8

import redis
# 连接Linux服务器上的redis

re = redis.Redis(host='192.168.178.115', port=6379)
re.set('key_name', 'value_tom')
re.set('key_name02', 'value_tom2')
re.set('key_name03', 'value_tom3')

print(re.get('key_name'))
print(re.get('key_name02'))
print(re.get('key_name03'))



