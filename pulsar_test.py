# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/18 10:41
@Auth ： 蔍鸣
@File ：pulsar_test.py
@IDE ：PyCharm
@Motto:拔丝kite博
"""

import pulsar
import json

import pulsar_thread as pt

client = pt.client('pulsar://localhost:6650')

#请将 0.0.0.0:6655 换成你的pulsar地址
