#!/usr/bin/env python 
#coding:utf-8

import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='password',db='s8')
cur=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

'''
sql = "update test set name=%s where name='Lee'"
params=('Aswill')
result=cur.execute(sql,params)
conn.commit()
result=cur.execute("select * from test")
data=cur.fetchall()
print data



sql = "insert into test values (%s)"
params=[('Bruce'),('Shelly')]
result=cur.executemany(sql,params)
conn.commit()
print cur.lastrowid #必须要使用自增ID
result=cur.execute("select * from test")
data=cur.fetchall()
print data
'''

sql = "select * from test"
result=cur.execute(sql)
data=cur.fetchall()
print data
#cur.scroll(0,mode='absolute') #绝对定位
cur.scroll(-2,mode='relative') #相对定位
data=cur.fetchone()
print data
print cur.lastrowid


cur.close()
conn.close()

