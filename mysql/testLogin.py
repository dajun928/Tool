#encoding=utf-8
from MysqlHelper import MysqlHelper
from hashlib import sha1

sname=raw_input("请输入用户名：")
spwd=raw_input("请输入密码:")

s1=sha1()
s1.update(spwd)
spwdSha1=s1.hexdigest()
sql="select upwd from userinfos where uname=%s"
params=[sname]
sqlhelper=MysqlHelper('127.0.0.1',3306,'test','root','1234')
userinfo=sqlhelper.get_one(sql,params)
if userinfo==None:
    print '用户名错误'
elif userinfo[0]==spwdSha1:
    print '登录成功'
else:
    print '密码错误'