#encoding=utf-8

from MysqlHelper import MysqlHelper


sname=["c","b","c","d"]

sql="insert into stu(name) values(%s)"

for name in sname:
    param = [name]

    MysqlHelper.insert(sql, param)

