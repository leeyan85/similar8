#!/usr/bin/env python 
#coding:utf-8
from model.admin import Admin

def main():
    username=raw_input('username')
    password = raw_input('password')
    admin = Admin()
    result=admin.CheckValidate(username)
    
    if not result:
        print "用户名密码错误"
    else:
        print "进入后台管理系统"
        
        
        
if __name__=="__main__":
    main()    