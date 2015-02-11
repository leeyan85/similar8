#coding: utf-8
f=file('myfile.txt','r')
for line in f.readlines():
    line = line.strip('\n').split(':')
    print line
    
f=file('myfile.txt','a')
f.write('\nnew line,hellworld')
f.close()

with file('myfile.txt','r') as f:
    for line in f: 
        print line