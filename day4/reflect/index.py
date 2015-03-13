#!/usr/bin/env python 
#coding:utf-8


#反射，当别的程序传入给你写的这段代码一个字符串，这个字符串是一个模块或者一个模块下的某个方法，你需要导入此模块或者方法，如何导入此模块或则方法呢
#如果直接执行 import ××× 是会出错的，因为×××在你的这段代码中是一个变量,这时就需要反射
'''
import backend.account
from Queue import Queue
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
   
    
    
class LeeException(Exception):
    def __init__(self,msg):
        self.error=msg
    def __str__(self,*args,**kwargs):
        return '自定义异常：LeeException'
    
obj=LeeException('异常')
print obj #用于调试，显示异常

def A():
    return 'abc'

try:
    res = A()
    print res
    if res == 'abc':
        print 'right'
    else:
        raise LeeException('异常')
except LeeException,e:
    print e


#例子，如何导入通过变量导入math模块
module="math"
MathModule=__import__(module)
print MathModule.pow(2,4)
import math
#例子通过变量导入方法
func="pow"
pow=getattr(MathModule,func)
print pow(2,4)
'''
import Queue
queue=Queue.Queue()

def ServerA():
    Dict={'server':'B','module':'math','func':'pow'}
    queue.put(Dict)
ServerA()

    
def ServerB():
    task=queue.get()
    #首先需要导入module
    if task['server']=='B':
        MathModule=__import__(task['module'])
        #其次在module中找到task['func']
        func=getattr(MathModule,task['func'])
        print func(2,4)
ServerB()    
运行ServerB函数, 执行相应的任务.

