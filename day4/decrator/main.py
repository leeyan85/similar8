#!/usr/bin/env python 
#coding:utf-8
#带参数的装饰器
def outer(f1,f2):
    def inner(func):
        def wrapper(arg):    
            f1()       
            result =  func(arg)
            f2()
            return result   
        return wrapper
    return inner


def login():
    print '验证开始'
    
def logout():
    print '验证完毕'

@outer(login,logout)
def func1(arg):
    print 'I am func1',arg
    return 'helloworld'

def func2():
    print 'i am func2'
  
def func3():
    print 'i am func3'    

if __name__=='__main__':
    result = func1('Lee')
    print result
    func2()
    func3()