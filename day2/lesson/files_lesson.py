#coding: utf-8
f=file('myfile.txt','r')
for line in f.readlines():
    line = line.strip('\n').split(':')
    print line
    
f=file('myfile.txt','a')
f.write('\nnew line,hellworld')
f.close()

with file('myfile.txt','r') as f:
    for line in f:  #迭代器，等同于f.xreadlines()，f.xreadlines()不推荐使用
        print 'xreadline',type(line)
        

for i in xrange(20):#xrange循环较大的类似于xreadlines,迭代器
    print i 
    
for i in range(20):#range生成一个列表
    print i     
    
with file('myfile.txt','r') as f:
    print type(f.readlines()) #读取所有文件，列表,每行作为一个列表元素
    print type(f.xreadlines()) #生成器，当需要读取时，才去取数据
    print type(f.readline()) #只读一行,字符串
    print type(f.read()) #读所有文件作为一个字符串