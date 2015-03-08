#!/usr/bin/env python 
#coding:utf-8
'''
import backend.account
data=raw_input('请输入：')
array=data.split('/')
package='backend.'
try:
    space = __import__(package+array[0])
    module = getattr(space,array[0])
    func = getattr(module,array[1])
    func()
except ImportError,e:
    print 1,e

except AttributeError,e:
    print 2,e
except Exception,e:
    print 3,e
else:
    print 'No exception'
finally:
    print "有无异常都要执行"
'''    
    
    
class MyException(Exception):
    def __init__(self,msg):
        self.error=msg
    def __str__(self,*args,**kwargs):
        return '自定义异常：MyException'
    
obj=MyException('异常')
print obj

