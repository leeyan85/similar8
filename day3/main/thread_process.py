#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import threading
import multiprocessing
import time
count_thread = 0
count_process = 0

# worker function
def worker1(sign, lock):
    global count_thread
    lock.acquire()
    count_thread += 1
    print(sign, os.getpid())
    lock.release()

def worker2(sign, lock):
    global count_process
    lock.acquire()
    count_process += 1
    print(sign, os.getpid())
    lock.release()
# Main
print('Main:',os.getpid())

# Multi-thread
record = []
lock  = threading.Lock()
for i in range(5):
    thread = threading.Thread(target=worker1,args=('thread',lock))
    thread.start()
    record.append(thread)
    time.sleep(2)

for thread in record:
    thread.join(1)

print count_thread