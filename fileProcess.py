#-*- coding:utf-8 -*-

import threading
import time

# glo_flag = 0
# # while True:
# def L():
#     global glo_flag
#     t()
#     print glo_flag
#     glo_flag += 10
#
# def t():
#     global glo_flag
#     glo_flag += 2
#     # print glo_flag
#
# L()
# print glo_flag
glo_flag = 0
while True:
    global glo_flag
    # 检测触摸停止按钮 主线程[多线程]
    #if 检测到被触摸:
        # if 1 场地触发 glo_flag = 1

        # if 2 场地触发 glo_flag = 2

        # if 3 场地触发 glo_flag = 3

        # if glo_flag == 1:
            # 调用 1 模块

        # if glo_flag == 2:
            # 调用 2 模块

        # if glo_flag == 3:
            # 调用 3 模块