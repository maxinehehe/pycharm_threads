#-*- coding:utf-8 -*-

import threading
import time
import thread

def return_num():
    for i in xrange(10):
        time.sleep(1)
        if i == 5:
            exit()
        print i,

def exitFunc():

    for i in xrange(20):
        print "exit:", i
    print "我将会退出"
    exit()
def main():
    t = threading.Thread(target=return_num, args=())
    t2 = threading.Thread(target=exitFunc, args=())

    t.start()
    t2.start()
# thread.start_new(touchmyhead, ())