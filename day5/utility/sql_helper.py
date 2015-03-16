#!/usr/bin/env python 
#coding:utf-8

import MySQLdb
import conf

class MysqlHelper(object):
    def __init__(self):
        self.__conn_dict=conf.dict_conn
    
    def GetAll(self):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cur.execute("select * from test")
        data=cur.fetchall()
        cur.close()
        conn.close()
        return data
    
    def GetOne(self,param):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql="select * from test where name=%s"
        param=(param)
        cur.execute(sql,param)      
        data=cur.fetchone()
        cur.close()
        conn.close()
        return data
    
class SqlServerHelper(object):
    def __init__(self):
        pass
    
    def GetAll(self):
        conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='password',db='s8')
        cur=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cur.execute("select * from test")
        data=cur.fetchall()
        cur.close()
        conn.close()
        return data
    
    def GetOne(self,param):
        conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='password',db='s8')
        cur=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql="select * from test where name=%s"
        param=(param)
        cur.execute(sql,param)      
        data=cur.fetchone()
        cur.close()
        conn.close()
        return data
