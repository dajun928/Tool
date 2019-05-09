#encoding=utf-8
from MysqlHelper import MysqlHelper


sname=[1,2,3,4]

sql="select * from stu "

for name in sname:
    param = [name]
    sqlhelper = MysqlHelper('127.0.0.1', 3306, 'test', 'root', '1234')
    # sqlhelper.insert(sql, param)
    print(sqlhelper.get_one(sql,param))
