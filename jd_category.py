import time
import pandas as pd
import re
from openpyxl import Workbook
import asyncio
import httpx

wb = Workbook()
ws = wb.active
ws.append(['商品ID', '类目'])

headers = {
    'authority': 'item.jd.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': '__jdu=16522482835401340221388; shshshfpa=76c25328-0cc5-ad08-acc1-cf2b162a0a61-1652248285; shshshfpb=mtdSJv___ru3iBB2r3XR1VA; pinId=qK9aQJjAmLWQcitARx7nPQ; __jdv=122270672|direct|-|none|-|1658399405916; areaId=12; ipLoc-djd=12-988-993-58088; PCSYCityID=CN_320000_320500_0; TrackID=1tIGnh0_iy90N-RnTWDVQYiNN5M7CvHS9e5bYZevT34Q-SliRcoek92HkopAdPqBkx4oD1vnh9qQS34JV4887PjeVg41-iHJ021jdUPMWspseXWAVrhzk-SNtdY6_Tt-A; pin=melody970315; unick=melody970315; _tp=KCNWsIWBBCQddTfrCDAtUg%3D%3D; _pst=melody970315; token=589bb9322b452c9f8deb1fcb89f87a89,2,921621; __jda=122270672.16522482835401340221388.1652248284.1658818579.1658918207.24; __jdb=122270672.1.16522482835401340221388|24.1658918207; __jdc=122270672; shshshfp=fff4866ab2a02bd418e6f9e85ec92b5d; shshshsID=b70894232252840a5931bcc0a00e9820_1_1658918208147; ip_cityCode=988; 3AB9D23F7A4B3C9B=WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM',
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
        async with httpx.AsyncClient(verify=False, timeout=30) as client:
            # 设置了https不验证和超时时间为30秒
            response = await client.get(url=f'https://item.jd.com/{g_id}.html', headers=headers)
            # print(type(response.text))
            category = re.findall(r'catName: (.*?)]', response.text)[0]
            print([g_id, category])
            ws.append([g_id, category])
            wb.save(r'./jd_category.xlsx')
    except Exception as e:
        print(e)


async def main():
    tasks = []
    df = pd.read_excel(r'./urls.xlsx')
    g_ids = df['商品ID']
    for g_id in g_ids:
       tasks.append(asyncio.create_task(get_data(g_id)))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    # async_start = time.time()
    asyncio.run(main())
    # async_end = time.time()
    # print(async_end - async_start)



