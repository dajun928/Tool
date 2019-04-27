#encoding=utf8
# 连接本地redis
import redis

re = redis.Redis(host='127.0.0.1', port=6379)
re.set('key_name', 'value_tom')
print(re.get('key_name'))



