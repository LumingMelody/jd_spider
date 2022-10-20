# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/16 11:34
@Auth ： 蔍鸣
@File ：ikun.py
@IDE ：PyCharm
@Motto:拔丝kite博
"""

import tkinter as tk
import random
import threading
import time


def boom():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('小黑子受死！！！！')
    window.geometry("200x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window, text='🐔霓太美', bg='green',
             font=('宋体', 17), width=20, height=4).pack()
    window.mainloop()


threads = []
for i in range(100):
    t = threading.Thread(target=boom)
    threads.append(t)
    time.sleep(0.1)
    threads[i].start()