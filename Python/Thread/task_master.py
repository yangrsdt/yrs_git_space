#!/usr/bin/python
# coding = utf8

import random,time,queue
from multiprocessing.managers import BaseManager

#发送任务的队列
send_task = queue.Queue()
#接收结果的队列
receive_result = queue.Queue()

#从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

#将上面两个队列注册到网络上,callable参数关联了Queue对象
QueueManager.register("send_task",callable=lambda :send_task)
QueueManager.register("receive_result",callable=lambda :receive_result)

#绑定端口5000,设置验证码为"abc"
manager = QueueManager(address=("",5000),authkey=b"abc")

#启动Queue
manager.start()

#获得通过网络访问的Queue对象
task = manager.send_task()
result = manager.receive_result()

#放几个任务进去
for i in  range(10):
    n = random.randint(0,10000)
    print("Put task %d..." % n)
    task.put(n)

#从result队列读取结果
print("Try to get results...")
for i in range(10):
    r = result.get(timeout=10)
    print("Result:%s" % r)

#关闭
manager.shutdown()

print("master exit...")