#!/usr/bin/python
# -*- coding:utf-8 -*-

import cx_Oracle

class DBHelper():
    def __init__(self):
        self.result=None
        try:
            self.db_conn = cx_Oracle.connect('用户名', '密码', '数据库地址:数据库端口/SID')
            self.cursor = self.db_conn.cursor()
        except Exception as e:
            print(e)

    def quary(self,sql):
        try:
            self.result=self.cursor.fetchall(sql)
            self.db_conn.commit()
            return self.result
        except Exception as e:
            print(sql)
            print(e)
        finally:
            self.cursor.close()
            self.db_conn.close()

    def execute(self,sql):
        try:
            self.cursor.execute(sql)
            self.db_conn.commit()
        except Exception as e:
            print(sql)
            print(e)
        finally:
            self.cursor.close()
            self.db_conn.close()

    def executemany(self,sql,list):
        try:
            self.cursor.executemany(sql, list)
        except Exception as e:
            print(sql)
            print(e)
        finally:
            self.cursor.close()
            self.db_conn.close()
