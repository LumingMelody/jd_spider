import json
import re
import time

import pandas as pd
import requests
from lxml import etree
from xlrd import sheet
from openpyxl import Workbook
from pymysql import *
import asyncio
from httpx import AsyncClient

# conn = connect(host='rm-uf664y8bsz73u37odio.mysql.rds.aliyuncs.com', port=3306, database='jd_notes', user='luming',
#                password='Luming1314', charset='utf8')
# cursor = conn.cursor()

wb = Workbook()
ws = wb.active
ws.append([
    '标题',
    '价格',
    '店铺',
    '商品ID',
    '备注',
    '详情页网址',
    '商品图片网址',
    '所有评论',
    '视频晒单',
    '好评',
    '中评',
    '差评',
    '追评',
    '好评率(%)',
])

headers = {
    # 'authority': 'item.jd.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '__jdu=16522482835401340221388; shshshfpa=76c25328-0cc5-ad08-acc1-cf2b162a0a61-1652248285; shshshfpb=mtdSJv___ru3iBB2r3XR1VA; qrsc=3; pinId=x75lWuiSpgVj0zC68MzCk7V9-x-f3wj7; __jdv=76161171|direct|-|none|-|1673591153320; areaId=12; rkv=1.0; ipLoc-djd=12-988-993-58088; pin=jd_40695e02c9f49; unick=jd_183256hzr; ceshi3.com=201; _tp=awBBMDETGlbi5IYojh4OKdV7sL7LjyuX5Q%2FfhbyGaHk%3D; _pst=jd_40695e02c9f49; TrackID=15200YZbJFQ2NqAPlmTKJwbw3xWMqnm7xiWnIqLsxEZaxmegeeK69-ctgP4-xi5WDcq3jIwWqvWDD50uvgHOr11gNpJ9bWZU1ocJ9Di2bKwr43GYLmNLvfYrQdpGU47dH; thor=6CE4A6B80C7882E3213DE3A0D63156A98E7B5C33DE19619491557C91EEDD578993DE69FE11D114B8D1B8910BCB9F0EB48D163DDD690BD633A39CA33A6AE97A57AD4D66FAE6A7495178B99D5846472D1F197C9B50821E9E33DB1D4CBFE18D13B9AF2127C423BA617C563509E67A1E134CE1AC3B1F5415F6CA9695EA2A34E8AA0D1BD40E28CC34CA6C2433C40D83A16B7D28BF00DAF4D953AE60266FA131A3BEF1; jsavif=1; __jda=76161171.16522482835401340221388.1652248284.1673836410.1673855556.62; __jdb=76161171.7.16522482835401340221388|62.1673855556; __jdc=76161171; shshshfp=2e9583f1d0b6c7a4b52623edc457fde3; shshshsID=1041948e5d3260d5db1a51c998258a73_5_1673855794044; 3AB9D23F7A4B3C9B=WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM',
    'referer': 'https://list.jd.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
}
headers_two = {
    'authority': 'npcitem.jd.hk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'shshshfpa=d8e043e2-d932-04de-aeac-363b38fe9aff-1661499467; shshshfpb=vKZ6Wnd2mtbwLm66Z47dhzA; pin=jd_40695e02c9f49; unick=jd_183256hzr; __jdc=181809404; __jdv=181809404|direct|-|none|-|1673855259413; areaId=12; ipLoc-djd=12-988-993-58088; thor=6CE4A6B80C7882E3213DE3A0D63156A98E7B5C33DE19619491557C91EEDD57892200675C8B9F1910E9714FCA8F3161E2578B27575EB4E5F9ADB5FA61D8815183604A85387B13406EF76491263F19F8F02BBF021C9983A1B335CBD8B7A49359AEBF570AC03C8DC9D3E4A37CFFC632AF07453A11FC818D4AF1B2D17148045B746A9777E7323824A66CF6075BB266C102E5374C854663531D196DFF0E52E3F1B595; shshshfp=b080b4ca20aca5430bcf14c0f8559c1d; __jda=181809404.1661499467174673487178.1661499467.1673855259.1673860644.3; 3AB9D23F7A4B3C9B=WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM; shshshsID=333a8ff2a2239d1191edcd213259af40_3_1673862724650; __jdb=181809404.3.1661499467174673487178|3.1673860644',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


async def get_jd_data(keyword, page):
    for i in range(1, 2):
        list_url = f'https://search.jd.com/Search?keyword={keyword}&qrst=1&stock=1&ev=exbrand_%E9%BB%9B%E7%8F%82%EF%BC%88DECORTE%EF%BC%89%5E&pvid=4cc26ac36e034bada71e0d62b443b4a2&page={page}&psort=3&click=0'
        async with AsyncClient(verify=False, timeout=30) as client:
            resp = await client.get(list_url, headers=headers)
            prices = re.findall(r'prices:\'(.*?)\',stocks', resp.text)
            prices = ','.join(prices).split(',')
            shop_names = re.findall(r'title=(.*?)>', resp.text)[2:]
            sku_ids = re.findall(r'data-spu="(.*?)"', resp.text)
            images = re.findall(r'data-lazy-img="(.*?)"', resp.text)[1:]
            for index, sku_id in enumerate(sku_ids):
                detail_url = f'https://npcitem.jd.hk/{sku_id}.html'
                response = await client.get(detail_url, headers=headers_two)
                title = re.findall(r'name: (.*?),', response.text)[0]
                try:
                    origin = re.findall(r'产地：(.*?)<', response.text)[0]
                except:
                    origin = ''
                image_url = 'https:' + str(images[index])
                ws.append([shop_names[index], title, prices[index], sku_id, detail_url, image_url, origin])
                print([shop_names[index], title, prices[index], sku_id, detail_url, image_url, origin])
        wb.save(rf'./data/jd_{keyword}.xlsx')


async def main():
    tasks = []
    df = pd.read_excel(r'./urls.xlsx')
    # g_ids = df['商品ID']
    keyword_list = df['关键词']
    for index, key_word in enumerate(keyword_list):
        tasks.append(asyncio.create_task(get_jd_data(key_word, index)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        print(e)
