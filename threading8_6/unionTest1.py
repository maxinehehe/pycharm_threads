# -*- coding:utf-8 -*-

# 利用多线程将1.识别红球 2.跌倒检测 3.识别后的动作 耦合
import callTest


def trackeBall(m):
    global x
    x = 10
    print x


if __name__ == '__main__':
    global x
    trackeBall(10)
    callTest.test()
