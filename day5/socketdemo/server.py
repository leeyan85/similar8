#!/usr/bin/env python 
#coding:utf-8
import socket

server = socket.socket()
ip_port=('127.0.0.1',9999)
server.bind(ip_port)
server.listen(5)

while True:
    conn,address=server.accept()
    print conn
    conn.send('hello,world')
    flag=True
    while flag:
        data=conn.recv(1024)
        print 'client %s%s' %(address[0],data)
        conn.send('SB')
        if data=="Lee":
            flag=False
    conn.close()
    
    
