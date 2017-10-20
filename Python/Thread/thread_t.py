#!/usr/bin/python
# coding = utf8

#多进程

##fork

import os

# print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
# pid = os.fork()
# print(pid)
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

##multiproessing

from  multiprocessing import Process

# def run_proc(name):
#     print("This child process is named %s(进程号：%s)" %(name,os.getpid()))
#
# if __name__ == "__main__":
#     print("Now,parent process's pid is %s" % os.getpid())
#     p = Process(target=run_proc,args=("test",))
#     p.start()
#     p.join()
#     print("END")

##Pool

from multiprocessing import Pool
import time,random

# def long_time_task(name):
#     print('Run task %s(进程号:%s)' % (name,os.getpid()))
#     start = time.time()
#     time.sleep(random.random())
#     end = time.time()
#     print('Task %s runs %0.3f seconds...' % (name,(end - start)))
#
# if __name__ == '__main__':
#     print("Parent process's pid %s..." % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print("Waiting for all subprocesses done...")
#     p.close()
#     p.join()
#     print("All subprocess done...")

##子进程

# import subprocess
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print(r)
#
# p = subprocess.Popen(["nslookup"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# o,e = p.communicate(b"set q=mx\npython.org\nexit\n")
# print(o.decode("utf8"))
# print(e.decode("utf8"))

##进程间通信

from multiprocessing import Queue
# def write(q):
#     print("Process to write is %s" % os.getpid())
#     for str in ["A","B","C"]:
#         print("Put %s to queue" % str)
#         q.put(str)
#         time.sleep(1)
#
# def read(q):
#     print("Process to read is %s" % os.getpid())
#     while 1:
#         str = q.get(1)
#         print("Get %s from queue" % str)
#
# if __name__ == "__main__":
#     print("Parent process is %s" % os.getpid())
#     q = Queue()
#     process_w = Process(target=write,args=(q,))
#     process_r = Process(target=read,args=(q,))
#     process_w.start()
#     process_r.start()
#     process_w.join()
#     process_r.terminate()

#多线程

##简单的使用

# n=0
# flag = False
#
# import threading
#
# def run_add():
#     print("Now,%s is running..." % threading.current_thread().name)
#     global n
#     global flag
#     if n == 20:
#         time.sleep(3)
#     while n<20:
#         n += 1
#         print("Now,%s is running,value is %d..." % (threading.current_thread().name,n))
#         time.sleep(1)
#
# def run_reduce():
#     print("Now,%s is running..." % threading.current_thread().name)
#     global n
#     while n<20:
#         if n == 0:
#             time.sleep(1)
#         n -= 1
#         global flag
#         print("Now,%s is running,value is %d..." % (threading.current_thread().name,n))
#         time.sleep(1)
#
#
#     print("%s is END..." % threading.current_thread().name)
#
# print("Now,%s is running..." % threading.current_thread().name)
# add = threading.Thread(target=run_add,name="Thread-run_add")
# reduce = threading.Thread(target=run_reduce,name="Tread-run_reduce")
# add.start()
# reduce.start()
# # reduce.join()
# print("%s is END..." % threading.current_thread().name)

##生产者与消费者

# from threading import Thread
# import queue
#
# queue_tmp = queue.Queue(10)
# class Producer(Thread):
#     def __init__(self, name):
#         Thread.__init__(self)
#         self.name = name
#
#     def run(self):
#         while 1:
#             queue_tmp.put(0)
#             print("Producer: %s create a product,number is %d..." % (self.name,queue_tmp.qsize()))
#             time.sleep(1)
#
#
# class Consumer(Thread):
#     def __init__(self, name):
#         Thread.__init__(self)
#         self.name = name
#
#     def run(self):
#         while 1:
#             queue_tmp.get()
#             print("Consumer: %s get a product,number is %d..." % (self.name,queue_tmp.qsize()))
#             time.sleep(1)
#
# def PCtest():
#     p1 = Producer("Producer-1")
#     c1 = Consumer("Consumer-1")
#     c2 = Consumer("Consumer-2")
#
#     p1.start()
#     c1.start()
#     c2.start()
#
# if __name__ == "__main__":
#     PCtest()


##Lock
# lock = threading.Lock()
#
# balance = 0
#
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(100000):
#         change_it(n)
#
# def run_thread(n):
#     for i in range(100000):
#         # 先要获取锁:
#         lock.acquire()
#         try:
#             # 放心地改吧:
#             change_it(n)
#         finally:
#             # 改完了一定要释放锁:
#             lock.release()
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

#ThreadLocal

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()


#进程 vs. 线程
