#!/usr/bin/env python
#coding: utf-8
def MyGenerator(*args):
    for i in args:
        yield i
def Lee(name,age):
    return 'I am %s,I am %d old' %(name,age)
def Marlon():
    return 'I am Marlon'
def Allen():
    return 'I am Allen'

function_list=  [Lee,Marlon,Allen]  
a=MyGenerator(*function_list)
print apply(a.next(),('Lee',29))
print apply(a.next())
print apply(a.next())


        
class MyIterator(object):
    def __init__(self,funcs):
        self.total_funcs=len(funcs)
        self.func_list=funcs
        self.step = 0
    def __iter__(self):
        pass
    def next(self):        
        if self.step < self.total_funcs:
            self.step+=1
            return self.func_list[self.step-1]
        else:
            raise StopIteration       
c=MyIterator(function_list)
print apply(c.next(),('Lee',29))
print apply(c.next())
print apply(c.next())