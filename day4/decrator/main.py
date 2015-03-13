#!/usr/bin/env python 
#coding:utf-8
def SeparatorLine():
    print "############################"

#装饰器带参数函数带参数    
def DecratorArgFuncArg(f1,f2):
    def inner(func):
        def wrapper(arg):
            print "装饰器带参数函数带参数"
            f1()       
            result =  func(arg)
            f2()
            return result   
        return wrapper
    return inner

#装饰器带参数函数不带参数
def DecratorArgFuncNoArg(f1,f2):
    def inner(func):
        def wrapper():
            print "装饰器带参数函数不带参数"
            f1()       
            result=func()
            f2()
            return result
        return wrapper
    return inner

#函数没有参数的装饰器
def FuncNoArgDecrator(func):
    def wrapper():
        print "函数没有参数的装饰器"       
        func()
    return wrapper

#函数有参数的装饰器
def FuncArgDecrator(func):
    def wrapper(arg):
        print "函数有参数的装饰器"       
        func(arg)
    return wrapper

#函数有返回值的装饰器
def FuncReturnDecrator(func):
    def wrapper():
        print "函数有返回值的装饰器"       
        result=func()
        return result
    return wrapper

#这两个函数用
def login():
    print '开始登录'
   
def logout():
    print '退出登录'

@FuncArgDecrator
def Lee(arg):
    print 'I am %s' %arg

@FuncNoArgDecrator
def Marlon():
    print 'i am Marlon'

@DecratorArgFuncNoArg(login,logout)
def Allen():
    print 'i am Allen'  

@DecratorArgFuncArg(login,logout)
def Aswill(name):
    print 'I am %s' %name  

@FuncReturnDecrator
def Frank():
    return 'I am frank'

if __name__=='__main__':
    SeparatorLine()
    Lee('Lee')
    SeparatorLine()
    Marlon()
    SeparatorLine()
    Allen()
    SeparatorLine()
    Aswill('Aswill')
    SeparatorLine()
    result = Frank()
    print result