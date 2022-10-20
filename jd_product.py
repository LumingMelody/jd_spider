import time

import pandas as pd
import requests
from lxml import etree
from openpyxl import Workbook

wb = Workbook()

ws = wb.active

ws.append(['商品ID', '商品标题'])

headers = {
    'authority': 'api.m.jd.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '__jdu=16522482835401340221388; shshshfpa=76c25328-0cc5-ad08-acc1-cf2b162a0a61-1652248285; shshshfpb=mtdSJv___ru3iBB2r3XR1VA; pin=melody970315; _tp=KCNWsIWBBCQddTfrCDAtUg%3D%3D; _pst=melody970315; unick=melody970315; pinId=qK9aQJjAmLWQcitARx7nPQ; TrackID=1Kc3pxR3Nd6uSuoZVdFNJH6JVdMWBMrTmhEP-dYQbFqWHugSRU6qYq__G2mqSfCMxJA8E3rl3y9e5SxHF8HgbV2VkrT_AneM4Ty5yU42hWmeuc5h4NQeF8voE8P2MJkYv; areaId=12; ipLoc-djd=12-988-993-58088; 3AB9D23F7A4B3C9B=WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM; visitkey=18132915493533146; wxa_level=1; retina=0; cid=9; jxsid=16564853395601470095; webp=1; __jdc=122270672; mba_muid=16522482835401340221388; sc_width=1920; _gia_s_local_fingerprint=0ae46c74aec797cc7d9305c405f737f5; shshshfp=d4e3d368d11177bee6c15c90f2bbed8b; equipmentId=WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM; fingerprint=0ae46c74aec797cc7d9305c405f737f5; deviceVersion=103.0.0.0; deviceOS=; deviceOSVersion=; deviceName=Chrome; _gia_s_e_joint={"eid":"WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM","ma":"","im":"","os":"Mac OS X","ip":"49.64.248.64","ia":"","uu":"","at":"5"}; sk_history=100038312444%2C; __jda=122270672.16522482835401340221388.1652248284.1656485339.1656487615.20; __wga=1656487616702.1656487616702.1656485340574.1656485340574.1.2; PPRD_P=UUID.16522482835401340221388-LOGID.1656487616732.1873416515; shshshsID=8366b3a31e28ea829ac47efa11f2e05f_1_1656487618232; warehistory="100038312444,100038312444,100038312444,100038312444,100038312444,100038312444,"; wqmnx1=MDEyNjM2M3B0ai9jMDRtbWNhbXVzdW09MSZlcGFzZzNqUEM2Zjg1M3o1YXN0YyBfcEs3SyBHIGUwUy82RjJuLTNRVU8qJkg%3D; __jdb=122270672.2.16522482835401340221388|20.1656487615; __jdv=122270672%7Ciosapp%7Ct_335139774%7Cappshare%7CCopyURL%7C1656487679801; mba_sid=16564876158036361363123918347.2',
    'origin': 'https://item.m.jd.com',
    'pragma': 'no-cache',
    'referer': 'https://item.m.jd.com/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}


def get_data(sku_id):
    url = f'https://item.m.jd.com/product/{sku_id}.html'
    print(url)
    response = requests.get(url, headers=headers)
    tree = etree.HTML(response.text)
    title = tree.xpath('//*[@id="itemName"]/text()')[0]
    print(title)
    ws.append([sku_id, title])
    wb.save('./石头g10_result.xlsx')

0
if __name__ == '__main__':
    df = pd.read_excel(r'./石头g10.xlsx')
    skus = df['skus']
    for sku in skus:
        if ',' in sku:
            sku = sku.split(',')[0]
        get_data(sku)
        time.sleep(1)
