#!/usr/bin/env python 
#coding:utf-8
import socket

client = socket.socket()
ip_port=('127.0.0.1',9999)

client.connect(ip_port)
data=client.recv(1024)
print data
while True:
    info=raw_input('client input:') 
    if info == 'exit':  
        break       
    else:
        client.send(info)
        data = client.recv(1024)
        print data
        
client.close()
        

