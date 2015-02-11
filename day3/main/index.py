#!/usr/bin/env python
#coding: utf-8
'''created by Lee Yan on Feb 8 2015'''
'''from file import demo

if __name__=='__main__':
    demo.Foo()
    
print __name__
print __file__
print __doc__'''

'''
def Foo(name,where,action):
    print '%s%s%s' %(name,where,action)
    

name=raw_input("请输入名字：").rstrip()    
Foo(where='北京',name=name,action='吃饭')
'''
def show(*args,**kwargs):
    for key in kwargs:
        print key,kwargs[key]
    for value in args:
        print value
        
value=[1,2,3,4]
dict_var={'Lee':29,'Marlon':27}
#show(name='Lee',action='asdf')
#show(*value,**dict_var)

'''
def Foo(*args):
    for item in args:
        yield item
        

a=Foo(*value)
#print 'asdfsd',Foo(*value).next()

print a.next()
print a.next()
#a=xrange(10)
#print 'asdfsd', a.next('')'''

result = 'gt' if 1>3 else 'lt'
print result
import math
temp=lambda x,y: x+y

print map(lambda x:pow(x,x),value)
print reduce(lambda x,y:x+y,value)
#print vars()

a=[1,2,4,4,5]
print filter(lambda x: x>1,a)
print map(lambda y: y+100,a)
print reduce(lambda x,y: x+y,a)


