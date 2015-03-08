#!/usr/bin/env python 
#coding:utf-8

class Father(object):#新式类
    def __init__(self):
        self.name='Liu'
        self.FamilyName='Yan'
        
    def Func(self):
        print 'Father.Func'
        
class Son(Father):
    def __init__(self):
        #Father.__init__(self)   #经典类执行父类构造函数
        super(Son,self).__init__()  #新式类执行父类构造函数
        self.name='Feng'
        
    def Bar(self):
        print 'Son.Bar'
    
    def Func(self):
        print 'Son overwrite the Father Func'
    
s1=Son()
print "inherit the father's FamilyName："+ s1.FamilyName
print s1.name
s1.Func()

