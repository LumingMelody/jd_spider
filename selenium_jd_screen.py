# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/26 15:46
@Auth ： 蔍鸣
@File ：selenium_jd_screen.py
@IDE ：PyCharm
@Motto:拔丝kite博
"""
import time

import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)  # 打开浏览器


def get_screen(sku_id):
    driver.get(f"https://item.jd.com/{sku_id}.html")  # 跳转至测试页面
    sleep(2)
    driver.maximize_window()
    time.sleep(1)
    driver.save_screenshot(rf"./data/{sku_id}.png")  # 截屏
    sleep(2)
    driver.close()


if __name__ == '__main__':
    df = pd.read_excel(r'./urls.xlsx')
    sku_ids = df['商品ID']
    for sku in sku_ids:
        get_screen(sku)
