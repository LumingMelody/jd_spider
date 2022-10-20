# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/16 11:04
@Auth ： 蔍鸣
@File ：jd_live_goods.py
@IDE ：PyCharm
@Motto:拔丝kite博
"""
import json
import time

from openpyxl import Workbook

import requests

wb = Workbook()
ws = wb.active
ws.append([
    "直播间ID", "直播标题", "直播时间", "统计日期", "商品名称", "商品ID", "父订单号", "子订单号", "下单用户名",
    "下单时间", "下单金额"
])

headers = {
    'authority': 'drlives.jd.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': '__jdu=16522482835401340221388; shshshfpa=76c25328-0cc5-ad08-acc1-cf2b162a0a61-1652248285; shshshfpb=mtdSJv___ru3iBB2r3XR1VA; ipLoc-djd=12-988-993-58088; unpl=JF8EAMBnNSttX00HV0sGHUYZHFRcW14PHB4GbzVWXApbQ1xXSFIaR0d7XlVdXhRKHh9uZBRUXVNIUQ4bAisSE3teVV1fDUIWAGpkNWRaWEIZRElPKxEQe1xkXloMSBQGZmQMVlldSlQHHgMYERBJVF1ubQ9LHjNvZgRRW15IXQwbCh4RF3ttUV5cCUIWAG5gB2RcaElVBB4LGRITTllkHzMISBQCbGIMVxBYTFAGGAcSERlJWVFfXQpOFgBsZwddVGhKZAY; visitkey=3994656252139739; retina=0; cid=9; webp=1; mba_muid=16522482835401340221388; __wga=1659410653279.1659410653279.1659410653279.1659410653279.1.1; __jdv=76161171%7Ckong%7Ct_2023480242_%7Ctuiguang%7C67bca57e8f89426f841cb9f299cba0df%7C1659410653287; sc_width=1920; shshshfp=d4e3d368d11177bee6c15c90f2bbed8b; _gia_s_local_fingerprint=2041c4652cbd66faeee02b9c0cd3f70e; equipmentId=WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM; fingerprint=2041c4652cbd66faeee02b9c0cd3f70e; deviceVersion=103.0.0.0; deviceOS=; deviceOSVersion=; deviceName=Chrome; _gia_s_e_joint={"eid":"WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM","ma":"","im":"","os":"Mac OS X","ip":"49.85.217.14","ia":"","uu":"","at":"5"}; sk_history=10047728819426%2C; 3AB9D23F7A4B3C9B=WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM; TrackID=1_LPZMXcKv6UNYuJMkbAw6LqNcmc68BQcJR6KzilFmGOmA2MEyXynx7AjN8niNLaoGudZhI4-q8GLGNljMBiYvKFyQb50XOoDidj3FmzrMYi3XUzvg9HhmDLm8QDS0n_e; thor=37EA597D6C725C1ED9A4AC9A92C00393DBC98DC5CF200830145E282474E105C34C45BE48D9136867501ECB0675620922F8CC48BD6A2033ED528FAC8F83281F947E2D458D9F1D59218C7A5454387C096ACCF78DAD0E4D26090361AF7673E575ED205CA8E219FD4E431852ED4502C3E20923D35CF7CDBA64E0E1494D3D2ED253B784718B22ADE8CFC896C543AAA1DCEAA740EFD6111DED088F15A6FA27D0AC0C18; pinId=PCUQqh2gZl-xWgI7hwRYvLV9-x-f3wj7; pin=jd_54348e1821194; unick=%E4%BA%AC%E8%87%B4Super%E8%B4%AD; ceshi3.com=000; _tp=sc4rJpFXCcbFB3h9TMpElYiW5vuleou7TwWUEfLXTJk%3D; logining=1; _pst=jd_54348e1821194; __jdc=256844112; auid=641740; autype=0; auname=%E4%BA%AC%E8%87%B4Super%E8%B4%AD; aupic=https%3A%2F%2Fstorage.360buyimg.com%2Fi.imageUpload%2F6a645f3534333438653138323131393431363338373830323631393539_big.jpg; disour=1; __jda=256844112.16522482835401340221388.1652248284.1660557237.1660616104.28',
    'origin': 'https://jlive.jd.com',
    'referer': 'https://jlive.jd.com/',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}


def get_data():
    data = '{"functionId":"getOrderDetailsData","map":{"guideType":"1","orderIds":"","startTime":"2022-08-15","endTime":"2022-08-15","page":2,"pageSize":10}}'

    response = requests.post('https://drlives.jd.com/liveGoodsAnalysis/generalData', headers=headers, data=data).json()
    total_page = response['soaResultMap']['data']['pageInfo']['totalPage']
    for page in range(0, int(total_page)):
        data = json.loads(data)
        data['page'] = page
        data = json.dumps(data)
        resp = requests.post('https://drlives.jd.com/liveGoodsAnalysis/generalData', headers=headers, data=data).json()
        print(resp)
        data_info = resp['soaResultMap']['data']['dataInfo']
        for d in data_info:
            # 直播间ID
            liveId = d['liveId']
            # 直播标题
            liveMainTitle = d['liveMainTitle']
            # 直播时间
            liveTime = d['liveTime']
            # 统计日期
            statisticalTime = d['statisticalTime']
            # 商品名称
            skuName = d['skuName']
            # 商品ID
            skuId = d['skuId']
            # 父订单号
            parentOrderId = d['parentOrderId']
            # 子订单号
            sonOrderId = d['sonOrderId']
            # 下单用户名
            orderAccount = d['orderAccount']
            # 下单时间
            orderedTime = d['orderedTime']
            # 下单金额
            orderAmount = d['orderAmount']
            ws.append([
                liveId, liveMainTitle, liveTime, statisticalTime, skuName, skuId, parentOrderId, sonOrderId,
                orderAccount, orderedTime, orderAmount
            ])
    time.sleep(1)
    wb.save(rf"./data/jd_live_goods_0815.xlsx")


if __name__ == '__main__':
    get_data()

