#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import threading
import multiprocessing
import time

#Process entry
def process_worker(sign,lock,function):
    global count_process
    #lock.acquire()
    count_process += 1
    print(sign, os.getpid())
    print apply(function)
    #lock.release()


#Thread entry
def thread_worker(sign, lock,function):
    global count_thread
    lock.acquire()
    count_thread += 1
    print(sign, os.getpid())
    print apply(function)
    lock.release()

    
#real work functions   
def Lee():
    return 'I am Lee'
def Marlon():
    return 'I am Marlon'
def Allen():
    return 'I am Allen'

    
count_thread = 0
count_process = 0
if __name__=='__main__':
    # Multi-process begin
    multiprocessing.freeze_support() #window python 中需要,否则会出现随意打开很多进程的情况
    print('Main:',os.getpid())
    record = []
    lock = multiprocessing.Lock()
    func_list = [Lee,Marlon,Allen]
    for function in func_list:        
        process = multiprocessing.Process(target=process_worker,args=('Process',lock,function))
        process.start()
        record.append(process)

    for process in record:
        process.join()   
    print "count_process value is", count_process #该值没有改变，多进程不共享内存
    

    # Multi-thread begin
    record = []
    lock  = threading.Lock()
    for function in func_list:  
        thread = threading.Thread(target=thread_worker,args=('thread',lock,function))
        thread.start()
        record.append(thread)

    for thread in record:
        thread.join()  
    
    print "count_thread value is", count_thread #该值改变，所以多线程共享内存

