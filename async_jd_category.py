import time
import asyncio
import aiohttp
import pandas as pd
import requests
import re

from lxml import etree
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.append(['商品ID', '类目'])

headers = {
    'authority': 'item.jd.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': '__jdu=16522482835401340221388; shshshfpa=76c25328-0cc5-ad08-acc1-cf2b162a0a61-1652248285; shshshfpb=mtdSJv___ru3iBB2r3XR1VA; pinId=qK9aQJjAmLWQcitARx7nPQ; TrackID=1Kc3pxR3Nd6uSuoZVdFNJH6JVdMWBMrTmhEP-dYQbFqWHugSRU6qYq__G2mqSfCMxJA8E3rl3y9e5SxHF8HgbV2VkrT_AneM4Ty5yU42hWmeuc5h4NQeF8voE8P2MJkYv; visitkey=18132915493533146; retina=0; cid=9; webp=1; mba_muid=16522482835401340221388; sc_width=1920; _gia_s_local_fingerprint=0ae46c74aec797cc7d9305c405f737f5; equipmentId=WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM; fingerprint=0ae46c74aec797cc7d9305c405f737f5; deviceVersion=103.0.0.0; deviceOS=; deviceOSVersion=; deviceName=Chrome; _gia_s_e_joint={"eid":"WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM","ma":"","im":"","os":"Mac OS X","ip":"49.64.248.64","ia":"","uu":"","at":"5"}; sk_history=100038312444%2C; __wga=1656487687272.1656487616702.1656485340574.1656485340574.2.2; unick=melody970315; token=9417578fc48bddb6053dc496b78b088b,3,921333; __tk=3d6e82ed02bfdb7b1ce8a05ca926369d,3,921333; jsavif=1; jsavif=1; shshshfp=fff4866ab2a02bd418e6f9e85ec92b5d; shshshsID=81095bf2ca1e8f275687741510f1cbbd_1_1658399405776; __jda=122270672.16522482835401340221388.1652248284.1656487615.1658399406.21; __jdb=122270672.1.16522482835401340221388|21.1658399406; __jdc=122270672; __jdv=122270672|direct|-|none|-|1658399405916; thor=2F3C97DA5B2E941EA18E198825D001610AE34EC4B3227B7A660104020D57BB5D3E35536D61366011C3309432AEA90B601BB5CD56C11EB9C74CEFDE8EF0741E9CD6385EC614D9B29349C8325EA154D947296C7C35C5AAA4C2FEB22B51D4B65FED93820095105A74D8FF3BF6B017E5694F26069EAB44B24266CC9C1A649596D54F22FFD1EF8A3BA7831B6AA3068739C323; ip_cityCode=988; ipLoc-djd=1-72-55653-0; 3AB9D23F7A4B3C9B=WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM',
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


# async def create_session():
#     return aiohttp.ClientSession()
#
#
# session = asyncio.get_event_loop().run_until_complete(create_session())


async def async_requests(g_id, semaphore):
    try:
        async with semaphore:
            async with aiohttp.ClientSession() as session:
                async with session.get(url=f'https://item.jd.com/{g_id}.html', headers=headers) as response:
                    # if response:
                    resp = await response.text()
                    # print(resp)
                    # response = requests.get(f'https://item.jd.com/{g_id}.html', headers=headers)
                    category = re.findall(r'catName: (.*?),        brand', resp)[0]
                    print([g_id, category])
                    ws.append([g_id, category])
                    # time.sleep(0.5)
    except Exception as e:
        print(g_id)
        print(e)


async def main():
    df = pd.read_excel(r'./urls.xlsx')
    g_ids = df['sku_id']
    semaphore = asyncio.Semaphore(500)
    tasks = [async_requests(gid, semaphore) for gid in g_ids]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
    wb.save(r'./data/jd_三菱_category.xlsx')

