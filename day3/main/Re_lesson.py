#coding: utf-8

'''
Created on 2015年2月12日

@author: leey
'''

#RE
import re
result1=re.match('\d+','abc987cnd123') #匹配开头
if result1 is None:
    print "nothing"
else:    
    print result1.group()

result2=re.search('\d+','123abc987cnd')#在整个字符串中寻找，找到第一个
if result2:
    print result2.group()

result3=re.findall('\d+','123abc987cnd')#找到所有的匹配返回列表
print result3

re_com1=re.compile('(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})')#分组查询
result4=re_com1.match('192.168.1.1')
if result4:
    print result4.groups()


src_str='localhost 127.0.0.1 nginx'
re_com2 = re.compile('(?P<hostname>\w+)\s+(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<appsoft>\w+)',)
m=re_com2.match(src_str)
print m.groupdict()
print m.group('ip'),m.group('hostname')


re_com3 = re.compile('127.0.0.1')
m = re_com3.sub('10.88.130.11',src_str)
print m
