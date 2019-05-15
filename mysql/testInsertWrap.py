#encoding=utf8
from MysqlHelper import *

sql='insert into stu(sname,time) values(%s,%s)'
sname=raw_input("请输入用户名：")
time=raw_input("请输入性别，1为男，0为女")
params=[sname,time]

mysqlHelper=MysqlHelper('127.0.0.1',3306,'test','root','1234')
count=mysqlHelper.insert(sql,params)
if count==1:
    print 'ok'
else:
    print 'error'