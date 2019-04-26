# -*- coding:utf-8 -*-

import RedisHelper

from MysqlHelper import mysql
from hashlib import sha1

name=raw_input("请输入用户名：")
pwd=raw_input("请输入密码：")

sha1=hashlib.sha1()
sha1.update(pwd)
pwd1=sha1.hexdigest()

try:
    redis=RedisHelper()
    if redis.get('uname')==name:
        print 'ok'
    else:
        mysql=MysqlHelper('127.0.0.1',3306,'test1','root','mysql')
        upwd=mysql.get_one('select upwd from userinfos where uname=%s',[name])
        if upwd==None:
            print '用户名错误'
        elif upwd[0]==pwd1:
            redis.set('uname', name)
            print '登录成功'
        else:
            print "密码错误"
except Exception,e:
    print e.message