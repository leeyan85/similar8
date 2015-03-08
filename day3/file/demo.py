#!/usr/bin/env python
#coding: utf-8

print 'demo', __name__

a=[1,2,4,4,5]
print filter(lambda x: x>1,a)
print map(lambda y: y+100,a)
print reduce(lambda x,y: x+y,a)
    
#以字符串的形式导入模块
module_name = 'sqlserver'
module = __import__(module_name)
module.Foo()

#以字符串的形式执行函数
func_name='Foo'
func = getattr(module,func_name)
func()

#根据字符串执行函数,执行运算表达式
eval('func("hello")')
print eval('8*8')


#随机生成验证码
import random
temp=random.randint(65,90)
print chr(temp)
checkcode_chr=[]

for i in range(6):   
    if i == random.randint(1,5):
        checkcode_chr.append(chr(random.randint(65,90)))
    else:
        checkcode_chr.append(str(random.randint(0,9)))
           
print checkcode_chr
checkcode=''.join(checkcode_chr)
print checkcode

#随机生成验证码2
import string
code=[]
a=string.ascii_letters+string.digits
for i in range(6):
    code.append(a[random.randint(0,len(a))])
print ''.join(code)     
    
 
#加密   
import hashlib
hash=hashlib.md5()
hash.update('admin')
print hash.hexdigest()


#序列化和json
import pickle
a={'Lee':29,'Frank':25}
with open('C:/python/SVNROOT/similar8/tmp/temp.txt','w') as f:
    pickle.dump(a,f)

















