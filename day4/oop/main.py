#!/usr/bin/env python 
#coding:utf-8
class Province(object):
    #静态字段
    desc = '中国一级行政区'
    
    #动态字段
    def __init__(self,name,capital,leader,flag=True): #定义专有方法__func__
        #动态字段,只有实例化的对象才能访问动态字段，类本身不能访问动态字段
        self.Name = name 
        self.Capital = capital 
        self.Leader = leader
        self.__Pollution = flag #私有变量定义__var
        self.Dict={'name':'Lee','age':30}

    #动态方法,或叫实例方法，只有实例化的对象才能访问动态方法
    def FrankDynamic(self):
        Province.LeeStatic()
        print 'This is 动态方法'
    
    #静态方法不能访问类变量和实例变量,相当于一个全局函数
    #类对象和类实例都可以访问静态方法,推荐使用类对象调用静态方法，在别的语言中强制使用类对象本身调用静态方法
    @staticmethod 
    def LeeStatic():
        print 'this is 静态方法'
    
    #特性，访问方式和字段的访问方式一样   
    @property
    def AllenProperty(self):
        return self.Name
    
    #类方法可以通过类对象或实例来调用的方法, 
    #不管你是用类对象还是实例调用这个方法,该方法的第一个参数总是定义该方法的类对象  
    @classmethod
    def MarlonClass(cls):
        print 'This is 类方法'
    
    #私有函数,只可以在动态方法中使用，也可以通过实例object._Province__sha调用，但请不要使用
    def __sha(self): 
        print 'This is 私有函数'
    
    def AswillDynamic(self): #可以通过动态方法调用私有函数
        
        self.__sha()
        

            
    @property #通过特性来访问动态私有字段，可以使用该装饰器，又叫特性
    def Pollution(self):
        print self.__Pollution
            
    @Pollution.setter #通过特性，修改动态私有字段,可以使用该装饰器，必须和上边的函数相结合
    def Pollution(self,value):
        self.__Pollution = value

    #常用的专有方法
    def __call__(self): #__call__专有方法
        print "this is call 方法"
        return "this is __str__专有方法"
   
    def __str__(self):
        return "this is __str__专有方法"
    
    def __getitem__(self,key):
        return self.Dict[key]
    
    def __setitem__(self,key,value):
        self.Dict[key]=value

    def __delitem__(self,key):
        del self.Dict[key]

        
####################以上是类的定义##############################
    
#实例化一个类对象               
HeiBeiProvince=Province('河北','石家庄','李扬',flag=False)
#类对象和实例都可以访问静态字段，静态字段最好使用类调用，不要使用实例调用
print HeiBeiProvince.desc #不推荐使用实例去调用静态字段或者方法
print Province.desc #推荐使用的类对象直接调用静态字段或者方法

HeiBeiProvince.FrankDynamic()

#类对象不能访问动态方法
#Province.FrankDynamic()

#类对象和类实例都可以访问静态方法LeeStatic,推荐使用类对象调用静态方法
Province.LeeStatic() 
HeiBeiProvince.LeeStatic()

#特性的访问方式
print HeiBeiProvince.AllenProperty #特性,可以像访问变量一样访问特性

#如何访问私有函数
HeiBeiProvince.AswillDynamic() #该公有函数去调用对象的私有函数__sha()

#通过特性访问修改私有变量
HeiBeiProvince.Pollution
HeiBeiProvince.Pollution=False
HeiBeiProvince.Pollution
HeiBeiProvince.MarlonClass()



#实例可以通过以下方法访问类的私有函数
HeiBeiProvince._Province__sha() #私有函数,可以通过这种方式访问，但坚决不要用在程序中



#专有方法的使用

#__call__,可以把类对象的实例当作函数使用
HeiBeiProvince() #把类对象的实例当作函数使用，相当于执行HeiBeiProvice.__call__()

#__str__
print HeiBeiProvince #会调用专有方法__str__

#__getitem__
print HeiBeiProvince['name']

#__setitem__
print 'before __setitem__', HeiBeiProvince['name']
HeiBeiProvince['name']='Frank'
print 'after __setitem__', HeiBeiProvince['name']

#__delitem__
del HeiBeiProvince['name']
print HeiBeiProvince.Dict


#专有变量__dict__
print HeiBeiProvince.__dict__

#专有变量__doc__
print HeiBeiProvince.__dict__