#!/usr/bin/env python
#coding: utf-8
def MyGenerator(*args):
    for i in args:
        yield i        
def Lee(name,age):
    return 'I am %s,I am %d old' %(name,age)
def Marlon(name):
    return 'I am %s' %(name)
def Allen(name):
    return 'I am %s' %(name)

function_list=  [Lee,Marlon,Allen]  
a=MyGenerator(*function_list)
print apply(a.next(),('Lee',29))
print apply(a.next(),('Marlon',))
return_value = apply(a.next(),('Allen',))
print return_value


        
class MyIterator(object):
    def __init__(self,step):
        self.step=step
    def __iter__(self):
        return self      
    def next(self):
        if self.step==0:
            raise StopIteration
        self.step-=1
        return self.step

c=MyIterator(4)
print c.next()
print c.next()
print c.next()
print c.next()