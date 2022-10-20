# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/26 15:34
@Auth ： 蔍鸣
@File ：playwright_screen.py
@IDE ：PyCharm
@Motto:拔丝kite博
"""
import asyncio
import pandas as pd
from playwright.async_api import async_playwright


async def get_screen(sku_id):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f"https://item.jd.com/{sku_id}.html")
        await page.screenshot(path=f'./data/{sku_id}.png')
        await browser.close()


if __name__ == '__main__':
    df = pd.read_excel(r'./urls.xlsx')
    sku_ids = df['商品ID']
    for sku in sku_ids:
        asyncio.run(get_screen(sku))
