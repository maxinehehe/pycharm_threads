#-*- coding:utf-8 -*-

# from time import ctime,sleep
#
# def music():
#     for i in range(2):
#         print "I was listening to music. %s" %ctime()
#         sleep(1)
#
# def move():
#     for i in range(2):
#         print "I was at the movies! %s" %ctime()
#         sleep(5)
#
# if __name__ == '__main__':
#     music()
#     move()
#     print "all over %s" %ctime()


import threading
from time import ctime,sleep


def music(func):
    # for i in range(2):
    print "I was listening to %s. %s" %(func,ctime())
        # sleep(1)

def move(func):
    # for i in range(2):
    print "I was at the %s! %s" %(func,ctime())
        # sleep(5)

threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()
    # while True:
    #     sleep(1)
    print "all over %s" %ctime()