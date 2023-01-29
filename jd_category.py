import time
import pandas as pd
import re
from openpyxl import Workbook
import asyncio
from httpx import AsyncClient

wb = Workbook()
ws = wb.active
ws.append(['商品ID', '类目', '店铺名称'])

headers = {
    'authority': 'item.jd.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': '__jdu=16522482835401340221388; shshshfpa=76c25328-0cc5-ad08-acc1-cf2b162a0a61-1652248285; shshshfpb=mtdSJv___ru3iBB2r3XR1VA; ipLoc-djd=12-988-993-58088; o2State={%22webp%22:true%2C%22lastvisit%22:1667298098695%2C%22avif%22:true}; __jdv=76161171|direct|-|none|-|1669366531883; PCSYCityID=CN_320000_320500_0; shshshfp=ad758aa637b38cc48f5f2ff22ea53cee; 3AB9D23F7A4B3C9B=WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM; wlfstk_smdl=rt2j4slxaffq733ry8rd3noizd3v59xx; TrackID=13RroK7WwY8uGnzcXTIvgO729myqCs5VRxELO1j3_iyViLyd5sKBKc2yn6dWZg8hSs9dl37sjio1IPxv5CEwlKEWgkx-Hmd3-GuqfzSEjLzQtDSeBOVilEk9aEmPNHLQj; thor=6CE4A6B80C7882E3213DE3A0D63156A98E7B5C33DE19619491557C91EEDD578960A3EC913F55CE3973A7C65A6EF283BD0ED239F3916DBB2D0C79F65982FD0EA1F309F8936A6C877421189C3DA679965FD4A5EDFEDC485F3E82A964DD683E8E78AF0F60B2A2673A7BA1EDEE81FE63BB1426F77FF1FC88C0938D4A1CC5CA6BA8E903DC6671485E487894F36993ED57ADEDA3392CC28B5D10C1B53589600AC2ACEC; pinId=x75lWuiSpgVj0zC68MzCk7V9-x-f3wj7; pin=jd_40695e02c9f49; unick=jd_183256hzr; ceshi3.com=201; _tp=awBBMDETGlbi5IYojh4OKdV7sL7LjyuX5Q%2FfhbyGaHk%3D; _pst=jd_40695e02c9f49; __jda=76161171.16522482835401340221388.1652248284.1667810820.1669366532.53; __jdc=76161171; __jdb=76161171.5.16522482835401340221388|53.1669366532; shshshsID=8a409ff04c720c41048960a7a6cbdc26_2_1669366582152',
    'pragma': 'no-cache',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}


async def get_data(g_id):
    try:
        async with AsyncClient(verify=False, timeout=30) as client:
            # 设置了https不验证和超时时间为30秒
            response = await client.get(url=f'https://item.jd.com/{g_id}.html', headers=headers)
            # print(type(response.text))
            category = re.findall(r'catName: (.*?)]', response.text)[0]
            shop_name = re.findall(r'target="_blank" title="(.*?)"', response.text)[0]
            print([g_id, category, shop_name])
            ws.append([g_id, category, shop_name])
            wb.save(r'./data/jd_得力_category1.xlsx')
            # time.sleep(2)
    except Exception as e:
        print(e)


async def main():
    tasks = []
    df = pd.read_excel(r'./urls.xlsx')
    g_ids = df['商品ID']
    for g in g_ids:
        # g_id = g.split('/')[-1].split('.')[0]
        # print(g_id)
        tasks.append(asyncio.create_task(get_data(g)))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    # async_start = time.time()
    asyncio.run(main())
    # async_end = time.time()
    # print(async_end - async_start)



