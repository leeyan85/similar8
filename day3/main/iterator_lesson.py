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
    def __init__(self,funcs):
        self.total_step=len(funcs)
        self.func_list=funcs
        self.step=0
    def __iter__(self):
        return self      
    def next(self):        
        if self.step < self.total_step :
            self.step+=1
            return self.func_list[self.step-1]
        else:
            raise StopIteration       
c=MyIterator(function_list)
print apply(c.next(),('Lee',29))
print apply(c.next(),('Marlon',))
print apply(c.next(),('Allen',))