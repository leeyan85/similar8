#!/usr/bin/env python 
#coding:utf-8

class Father(object):#新式类
    def __init__(self):
        self.name='Liu'
        self.FamilyName='Yan'
        
    def Lee(self):
        print '我是父类函数Lee'
    
    def Allen(self):
        print "我是父类函数Allen"
        
class Son(Father):
    def __init__(self):
        #Father.__init__(self)   #经典类执行父类构造函数
        super(Son,self).__init__()  #新式类执行父类构造函数
        self.name='Feng'
        
    def Bar(self):
        print 'Son.Bar'
    
    def Lee(self):#重写父类函数Lee
        print '子类重写了父类函数Lee'
    
s1=Son()
print "继承了父类的姓"+ s1.FamilyName
print "重写了父类的名字",s1.name
s1.Lee() #子类重写了父类函数Lee
s1.Allen() #子类继承了父类函数Allen

