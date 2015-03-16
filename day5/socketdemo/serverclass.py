#!/usr/bin/env python 
#coding:utf-8
import SocketServer


class Myserver(SocketServer.BaseRequestHandler):
    def handle(self):
        while True:
            conn=self.request
            address=self.client_address
            print conn
            conn.send('hello,world')
            flag=True
            while flag:
                data=conn.recv(1024)
                print 'client %s%s' %(address[0],data)                
                if data=='exit':
                    flag=False
                else:
                    conn.send('SB')
        conn.close()
    
    def finish(self):
        pass
    

if __name__=="__main__":
    server=SocketServer.ThreadingTCPServer(('127.0.0.1',9999),Myserver)
    server.serve_forever()
    