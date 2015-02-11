#coding: utf-8
a = ['',1,2,3,4,5,6,7,8,9,9,2,3,2,4,2,54,2,65,2,5,6,2]
print a[0:5]
print a[1::2]
a = ['c','a']
a='asfdsfd'
print ' '.join('hellword')

'''pos=0
for i in range(a.count(2)):
    if pos==0:
        pos = pos + a.index(2)
    else:
        pos=a.index(2,pos+1)
    print 'find position', pos


first_pos=0
for i in range(a.count(2)):
    new_list=a[first_pos:]
    next_pos = new_list.index(2) + 1
    print 'find positions',first_pos + new_list.index(2)
    first_pos += next_pos'''