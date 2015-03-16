#!/usr/bin/env python 
#coding:utf-8

from utility.sql_helper import MysqlHelper

class Admin(object):
    def __init__(self):
        self.__helper=MysqlHelper()
    def GetOne(self,sql,param):
        return self.__helper.GetOne(sql,param)
    
    def CheckValidate(self,username):
        sql = 'select * from test where username=%s'
        params = (username)
        return self.__helper.GetOne(username)
        