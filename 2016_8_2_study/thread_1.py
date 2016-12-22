#-*- coding:utf-8 -*-

import threading
import time

def func1(x,y):
    for i in xrange(x,y):
        print i
    # time.sleep(5)

t1 = threading.Thread(target=func1,args=(15,23))
t1.start()
t1.join(5)#5表示等待时长

t2 = threading.Thread(target=func1,args=(5,20))
t2.start()
# t2.join()

print 't1',t1.isAlive()
print 't2',t2.isAlive()
'''
15
16
17
18
19
5
6
7
8
9
'''
