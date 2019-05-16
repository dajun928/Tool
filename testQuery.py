# -*- coding:utf-8 -*-

import MySQLdb

try:
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='1234', db='test')
    cur=conn.cursor()
    cur.execute('select * from stu')
    result = cur.fetchall()

    print result
    # for i in result.items():
    # print (i)

    conn.commit()
    cur.close()
    conn.close()
except Exception,e:
    print e.message
