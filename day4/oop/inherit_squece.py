#!/usr/bin/env python 
#coding:utf-8
#经典类继承是深度优先，是一个BUG, 新式类是广度优先，应该是用新式类

class A():
    def __init__(self):
        print 'This is from A'
    
    def test(self):
        print 'This is test from A'

class B(A):
    def __init__(self):
        print "This is from B"
        

class C(A):
    def __init__(self):
        print "This is from C"
    
    def test(self):
        print "This is test from C"
        
        
class D(B,C):
    def __init__(self):
        print 'this is D'
        
T1=D()
T1.test()

#抽象类加抽象方法就等于面向对象编程中的接口
from abc import ABCMeta,abstractmethod

class interface(object):
    __metaclass__ = ABCMeta   
    @abstractmethod
    def Lee(self):
        pass

class RelalizeInterface(interface):
    def __init__(self):    
        print '这是接口interface的实现'
    def Lee(self):
        print '实现'
    
sender = RelalizeInterface()
sender.send()


