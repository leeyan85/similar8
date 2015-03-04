#!/usr/bin/env python
#coding: utf-8
#定义三个函数        
def Lee(name,age):
    return 'I am %s,I am %d old' %(name,age)
    
def Marlon():
    return 'I am Marlon'
    
def Allen():
    return 'I am Allen'
    
function_list=  [Lee,Marlon,Allen]  #有三个函数的列表

#定义一个生成器 
def MyGenerator(*args):
    for i in args:
        yield i
        
a=MyGenerator(*function_list) #生成器
print apply(a.next(),('Lee',29)) #执行next()方法，这时会保存现在的执行状态，下一次调用next()方法时，会用到此状态
print apply(a.next())
print apply(a.next())

#为什么yield有next方法？ 看下面迭代器的列子，就会明白为什么生成器是由迭代器实现的
#下面是迭代器的例子， 一个类如果实现了__iter__方法,和next()方法，就叫做迭代器      
class MyIterator(object):
    def __init__(self,funcs):
        self.total_funcs=len(funcs)#记录总共需要执行多少个函数
        self.func_list=funcs #记录所有函数
        self.step = 0 #记录当前执行到哪一个函数
    def __iter__(self):
        pass
    def next(self):        
        if self.step < self.total_funcs: #当目前所执行的函数所在的位置小于总的函数个数时
            self.step+=1 #step
            return self.func_list[self.step-1] #执行当前函数
        else:
            raise StopIteration       

c=MyIterator(function_list)
print apply(c.next(),('Lee',29))
print apply(c.next())
print apply(c.next())