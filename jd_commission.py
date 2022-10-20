# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/18 11:37
@Auth ： 蔍鸣
@File ：jd_commission.py
@IDE ：PyCharm
@Motto:拔丝kite博
"""
import datetime
import time

import requests
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.append([
    "直播间ID", "直播标题", "开播时间", "有效引入订单量", "有效引入订单金额", "预估佣金"
])

headers = {
    'authority': 'drlives.jd.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': '__jdu=16522482835401340221388; shshshfpa=76c25328-0cc5-ad08-acc1-cf2b162a0a61-1652248285; shshshfpb=mtdSJv___ru3iBB2r3XR1VA; ipLoc-djd=12-988-993-58088; unpl=JF8EAMBnNSttX00HV0sGHUYZHFRcW14PHB4GbzVWXApbQ1xXSFIaR0d7XlVdXhRKHh9uZBRUXVNIUQ4bAisSE3teVV1fDUIWAGpkNWRaWEIZRElPKxEQe1xkXloMSBQGZmQMVlldSlQHHgMYERBJVF1ubQ9LHjNvZgRRW15IXQwbCh4RF3ttUV5cCUIWAG5gB2RcaElVBB4LGRITTllkHzMISBQCbGIMVxBYTFAGGAcSERlJWVFfXQpOFgBsZwddVGhKZAY; visitkey=3994656252139739; retina=0; cid=9; webp=1; mba_muid=16522482835401340221388; __wga=1659410653279.1659410653279.1659410653279.1659410653279.1.1; sc_width=1920; shshshfp=d4e3d368d11177bee6c15c90f2bbed8b; _gia_s_local_fingerprint=2041c4652cbd66faeee02b9c0cd3f70e; equipmentId=WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM; fingerprint=2041c4652cbd66faeee02b9c0cd3f70e; deviceVersion=103.0.0.0; deviceOS=; deviceOSVersion=; deviceName=Chrome; _gia_s_e_joint={"eid":"WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM","ma":"","im":"","os":"Mac OS X","ip":"49.85.217.14","ia":"","uu":"","at":"5"}; sk_history=10047728819426%2C; pinId=PCUQqh2gZl-xWgI7hwRYvLV9-x-f3wj7; unick=%E4%BA%AC%E8%87%B4Super%E8%B4%AD; ceshi3.com=000; _tp=sc4rJpFXCcbFB3h9TMpElYiW5vuleou7TwWUEfLXTJk%3D; logining=1; _pst=jd_54348e1821194; wlfstk_smdl=o59ws542xbfkpmusg94goznbs8lzf9o4; __jdv=256844112|direct|-|none|-|1660793662275; 3AB9D23F7A4B3C9B=WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM; TrackID=1p5Q8JRDU0Et8aUemybgOucudYFRS9SHvE4y4aZcRIjYZhjjtej8tcY5yFGL59dQ6ccOmQTT-Petx-P7JR9kYj4MpGfm_lZCDDhUKjOnU8NXQFAJmw26uIh7XuIzIjq0r; thor=37EA597D6C725C1ED9A4AC9A92C00393DBC98DC5CF200830145E282474E105C337D0D5BE6CDBBE257C4CD3FC7AED5626C97B7255D14E0272D33A019DFBA849E1ECF3D7324AE71D86164E99772DDC53552D33D20620DFA970C4E118F1586A507746EE5FB253D110724EE6EC9977683AEA111AB756FC05EAFF88145EA62E0634CE48AA370192776A3A6EFF9D5D16D9A436A1019A5B8F54C36FAFFC9D0CA5FD8AAF; pin=jd_54348e1821194; __jda=256844112.16522482835401340221388.1652248284.1660702414.1660793662.32; __jdc=256844112; auid=641740; autype=0; auname=%E4%BA%AC%E8%87%B4Super%E8%B4%AD; aupic=https%3A%2F%2Fstorage.360buyimg.com%2Fi.imageUpload%2F6a645f3534333438653138323131393431363338373830323631393539_big.jpg; disour=1; __jdb=256844112.6.16522482835401340221388|32.1660793662',
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
    data = '{"functionId":"offLineLiveDetailList","map":{"download":false,"pageSize":10,"startTimeStamp":1659283200000,"endTimeStamp":1660751999999,"page":1,"liveIdStr":null}}'

    response = requests.post('https://drlives.jd.com/LiveDataCpsOffline/generalData', headers=headers, data=data).json()
    liveDetailList = response['soaResultMap']['data']['liveDetailList']
    for l in liveDetailList:
        liveId = l['liveId']
        ts = l['startTime']
        s_ts = time.localtime(int(ts / 1000))
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", s_ts)
        title = l['title']
        totalEstimateEarningInRoom = l['totalEstimateEarningInRoom']
        totalOrderNumInRoom = l['totalOrderNumInRoom']
        totalOrderPriceInRoom = l['totalOrderPriceInRoom']
        ws.append([liveId, title, start_time, totalOrderNumInRoom, totalOrderPriceInRoom, totalEstimateEarningInRoom])
    wb.save(r'./data/jd_commission.xlsx')


if __name__ == '__main__':
    get_data()
