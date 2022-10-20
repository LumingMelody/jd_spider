# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/29 15:14
@Auth ： 蔍鸣
@File ：jd_weibo.py
@IDE ：PyCharm
@Motto:拔丝kite博
"""
import re
from openpyxl import Workbook

import requests

wb = Workbook()
ws = wb.active
ws.append([
    '用户名', '用户链接'
])
headers = {
    'authority': 'event.weibo.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'SINAGLOBAL=9857705707768.893.1644812593989; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWndaMrC7jCK8pQ3JIVbkC45JpX5KMhUgL.FoMfehq4eKqNShM2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNSK5c1K2cS0BN; UOR=,,www.jianshu.com; ULV=1659098076272:9:3:2:2743936140828.871.1659098076183:1658814000122; PC_TOKEN=f37dc81ee7; ALF=1693293079; SSOLoginState=1661757081; SCF=Ar0f7QlI9sKKIftdDT1kGZM6uQ9XcIwsjysIo7IBL1yc2frfVzR37GhcFvcnnlv2ls0mSyyqDarY6LxBq36WN1o.; SUB=_2A25OCBbKDeRhGeFL61QY8SjLzzuIHXVtfA8CrDV8PUNbmtAKLVmmkW9NQoYgC4LtRoe4jTEd83VCAP0OdAmYbZh0; ariaReadtype=1; ariaStatus=true; WBStorage=4d96c54e|undefined',
    'pragma': 'no-cache',
    'referer': 'https://event.weibo.com/yae/event/lottery/result?id=14130401&pageid=100140Ee687947',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


def get_data(page):
    url = f'https://event.weibo.com/yae/aj/event/lottery/result?pageid=100140Ee687947&id=14130401&page={page}'
    response = requests.get(url, headers=headers).json()
    html = response['data']['html']
    print(html)
    print(type(html))
    for i in range(0, 9, 3):
        user_url = "https:" + re.findall(r"a target='_blank' href=(.*?)>", html)[i]
        # user_url_two = re.findall(r"a target='_blank' href=(.*?)>", html)[2]
        # user_url_three = re.findall(r"a target='_blank' href=(.*?)>", html)[4]
        if i == 0:
            j = 0
        elif i == 3:
            j = 1
        else:
            j = 2
        user_name = re.findall(r"class='S_txt1'>(.*?)<", html)[j]
        # user_name_two = re.findall(r"class='S_txt1'>(.*?)<", html)[1]
        # user_name_three = re.findall(r"class='S_txt1'>(.*?)<", html)[2]
        ws.append([user_name, user_url])
    wb.save(r'./data/jd_weibo_1.xlsx')


if __name__ == '__main__':
    for p in range(17, 18):
        get_data(p)
