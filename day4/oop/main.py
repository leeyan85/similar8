#!/usr/bin/env python 
#coding:utf-8
class Province(object):
    #静态字段
    memo = '中国的23个省之一'
    __private = 'This is 静态私有变量'   
    
    #动态字段
    def __init__(self,name,capital,leader,flag=True):
        self.Name = name
        self.Capital = capital
        self.Leader = leader
        self.__Thailand = flag #私有变量
   
    #动态方法,或叫对象方法
    def SportsAction(self):
        print 'This is 动态方法'    
    
    #静态方法,去掉则编译报错;还有静态方法不能访问类变量和实例变量
    #不需要定义实例即可使用这个方法。另外，多个实例共享此静态方法
    @staticmethod
    def Foo():
        print 'this is 静态方法'
    
    #特性，访问方式和字段的访问方式一样   
    @property
    def Bar(self):
        return self.Name
    
    #类方法，一个类方法就可以通过类或它的实例来调用的方法, 
    #不管你是用类来调用这个方法还是类实例调用这个方法,该方法的第一个参数总是定义该方法的类对象  
    @classmethod
    def Demo(cls):
        print 'This is 类方法'
    
    #私有函数
    def __sha(self):
        print '私有函数'
    
    def Foo2(self): #通过它调用有函数
        self.__sha()
        
    #读动态私有字段
    @property
    def Thailand(self):
        print self.__Thailand
    
    #写动态私有字段
    @Thailand.setter
    def Thailand(self,value):
        self.__Thailand = value

    def __call__(self):
        print "this is call 方法"
           
hb=Province('河北','石家庄','李扬')

#类不能访问动态字段
#Province.Name

#对象可以访问静态字段
print hb.memo
hb.SportsAction()

#类不能访问动态方法
#Province.SportsAction()

#对象和类都可以访问静态方法Foo
Province.Foo()
hb.Foo()


print hb.Bar #特性

hb.Foo2() #该公有函数去调用对象的私有函数__sha()

#如何修改访问私有变量
hb.Thailand
hb.Thailand=False
hb.Thailand

hb() #执行类的__call__方法,把类的对象当作函数使用
