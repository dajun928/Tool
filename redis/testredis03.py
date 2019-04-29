#encoding=utf8

import redis
# 连接Linux服务器上的redis

re = redis.Redis(host='192.168.178.115', port=6379)

# pipe = re.pipeline()
# pipe.set('name', 'world')
# pipe.get('name')
# pipe.execute()

# print(re.get('name'))


# pipe = re.pipeline()
# pipe.set('wlt-spider', 'world')
# pipe.set('wlt-spider', 'world2')
# pipe.set('wlt-spider', 'world3')
# pipe.set('wlt-spider', 'world4')
# pipe.set('wlt-spider', 'world5')
# pipe.execute()
# print(re.get('wlt-spider'))

for i in range(100):
    # print i
    re.lpush('spider', '%d' % i)

# re.append('wlt-spider', 'ggsaggfg')

# print(re.get('spider'))
# for i in range(100):
#     print i
#     re.lpush('wlt-spider', '%d' % i)

print(re.llen('spider'))
lst=re.lrange('spider',0,-1)
lst.reverse()
print(lst)







