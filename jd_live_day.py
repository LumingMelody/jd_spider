# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/16 10:19
@Auth ： 蔍鸣
@File ：jd_live_day.py
@IDE ：PyCharm
@Motto:拔丝kite博
"""
import json
from openpyxl import Workbook

import requests

wb = Workbook()
ws = wb.active
ws.append([
    "直播间ID", "直播标题", "开播方式", "直播时间", "统计日期", "直播观看人次", "直播观看人数", "点赞次数", "点赞人数",
    "评论次数", "评论人数", "分享次数", "分享人数", "关注店铺人数", "关注主播人数", "引导进商详次数", "引导进商详人数",
    "引导加购次数", "引导加购人数", "引导进店次数", "引导进店人数", "人均停留时长（秒）", "引导成交父单量",
    "引导成交子单量",
    "引导成交商品件数", "引导成交金额", "引导成交人数", "引导7日成交父单量", "引导7日成交子单量", "引导7日成交商品件数",
    "引导7日成交金额", "引导7日成交人数", "引导15日成交父单量", "引导15日成交子单量", "引导15日成交商品件数",
    "引导15日成交金额",
    "引导15日成交人数",
])

headers = {
    'authority': 'drlives.jd.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': '__jdu=16522482835401340221388; shshshfpa=76c25328-0cc5-ad08-acc1-cf2b162a0a61-1652248285; shshshfpb=mtdSJv___ru3iBB2r3XR1VA; ipLoc-djd=12-988-993-58088; unpl=JF8EAMBnNSttX00HV0sGHUYZHFRcW14PHB4GbzVWXApbQ1xXSFIaR0d7XlVdXhRKHh9uZBRUXVNIUQ4bAisSE3teVV1fDUIWAGpkNWRaWEIZRElPKxEQe1xkXloMSBQGZmQMVlldSlQHHgMYERBJVF1ubQ9LHjNvZgRRW15IXQwbCh4RF3ttUV5cCUIWAG5gB2RcaElVBB4LGRITTllkHzMISBQCbGIMVxBYTFAGGAcSERlJWVFfXQpOFgBsZwddVGhKZAY; visitkey=3994656252139739; retina=0; cid=9; webp=1; mba_muid=16522482835401340221388; __wga=1659410653279.1659410653279.1659410653279.1659410653279.1.1; __jdv=76161171%7Ckong%7Ct_2023480242_%7Ctuiguang%7C67bca57e8f89426f841cb9f299cba0df%7C1659410653287; sc_width=1920; shshshfp=d4e3d368d11177bee6c15c90f2bbed8b; _gia_s_local_fingerprint=2041c4652cbd66faeee02b9c0cd3f70e; equipmentId=WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM; fingerprint=2041c4652cbd66faeee02b9c0cd3f70e; deviceVersion=103.0.0.0; deviceOS=; deviceOSVersion=; deviceName=Chrome; _gia_s_e_joint={"eid":"WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM","ma":"","im":"","os":"Mac OS X","ip":"49.85.217.14","ia":"","uu":"","at":"5"}; sk_history=10047728819426%2C; 3AB9D23F7A4B3C9B=WIU2U435OV5RTO6JZY6R7QHUM4E5VZHLJ3JDIHJTCABS4HKSIPTPE3A6ALJVTRH4RHAAKZ53CN3Q24H7GXN3YUXRJM; TrackID=1_LPZMXcKv6UNYuJMkbAw6LqNcmc68BQcJR6KzilFmGOmA2MEyXynx7AjN8niNLaoGudZhI4-q8GLGNljMBiYvKFyQb50XOoDidj3FmzrMYi3XUzvg9HhmDLm8QDS0n_e; thor=37EA597D6C725C1ED9A4AC9A92C00393DBC98DC5CF200830145E282474E105C34C45BE48D9136867501ECB0675620922F8CC48BD6A2033ED528FAC8F83281F947E2D458D9F1D59218C7A5454387C096ACCF78DAD0E4D26090361AF7673E575ED205CA8E219FD4E431852ED4502C3E20923D35CF7CDBA64E0E1494D3D2ED253B784718B22ADE8CFC896C543AAA1DCEAA740EFD6111DED088F15A6FA27D0AC0C18; pinId=PCUQqh2gZl-xWgI7hwRYvLV9-x-f3wj7; pin=jd_54348e1821194; unick=%E4%BA%AC%E8%87%B4Super%E8%B4%AD; ceshi3.com=000; _tp=sc4rJpFXCcbFB3h9TMpElYiW5vuleou7TwWUEfLXTJk%3D; logining=1; _pst=jd_54348e1821194; __jdc=256844112; auid=641740; autype=0; auname=%E4%BA%AC%E8%87%B4Super%E8%B4%AD; aupic=https%3A%2F%2Fstorage.360buyimg.com%2Fi.imageUpload%2F6a645f3534333438653138323131393431363338373830323631393539_big.jpg; disour=1; __jda=256844112.16522482835401340221388.1652248284.1660557237.1660616104.28; __jdb=256844112.2.16522482835401340221388|28.1660616104',
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
    data = '{"page":1,"pageSize":5,"liveStartTime":"2022-08-15","liveEndTime":"2022-08-15"}'
    # print(type(data))
    response = requests.post('https://drlives.jd.com/core/getBasicDataTableArea', headers=headers, data=data).json()
    total = response['data']['pagination']['total']
    if total % 10 > 0:
        page_num = int(total / 5) + 1
    else:
        page_num = int(total / 5)
    # print(page_num)
    if page_num >= 1:
        for i in range(1, page_num):
            data = json.loads(data)
            data['page'] = i
            data = json.dumps(data)
            resp = requests.post('https://drlives.jd.com/core/getBasicDataTableArea', headers=headers, data=data).json()
            result = resp['data']['list']
            for r in result:
                # 直播间ID
                content_id = r['contentId']
                # 直播标题
                content_main_title = r['contentMainTitle']
                # 开播方式
                liveBroadcastWay = r['liveBroadcastWay']
                # 直播开始时间
                liveStartTm = r['liveStartTm']
                # 直播结束时间
                liveEndTm = r['liveEndTm']
                # 统计日期
                dt = r['dt']
                # 直播观看人次
                pv = r['pv']
                # 直播观看人数
                uv = r['uv']
                # 点赞次数
                liveLikeCnt = r['liveLikeCnt']
                # 点赞人数
                liveLikeUserQtty = r['liveLikeUserQtty']
                # 评论次数
                explainreplyCnt = r['explainreplyCnt']
                # 评论人数
                explainreplyUserQtty = r['explainreplyUserQtty']
                # 分享次数
                shareCnt = r['shareCnt']
                # 分享人数
                shareUserQtty = r['shareUserQtty']
                # 关注店铺次数
                anchorFollowCnt = r['anchorFollowCnt']
                # 关注主播人数
                anchorFollowUserQtty = r['anchorFollowUserQtty']
                # 引导进商详次数
                skuPv = r['shopPv']
                # 引导进商详人数
                skuUv = r['shopUv']
                # 引导加购次数
                contentCartSkuAmount = r['contentCartSkuAmount']
                # 引导加购人数
                contentCartUv = r['contentCartUv']
                # 引导进店次数
                shopPv = r['shopPv']
                # 引导进店人数
                shopUv = r['shopUv']
                # 人均停留时长(秒)
                avgStmRt = r['avgStmRt']
                # 引导成交父单量
                content1DayPntCwOrdNum = r['content1DayPntCwOrdNum']
                # 引导成交子单量
                content1DayCwOrdNum = r['content1DayCwOrdNum']
                # 引导成交商品件数
                content1DayCwOrdGoods = r['content1DayCwOrdGoods']
                # 引导成交金额
                content1DayCwOrdAmount = r['content1DayCwOrdAmount']
                # 引导成交人数
                content1DayCwOrdUsers = r['content1DayCwOrdUsers']
                # 引导7日成交父单量
                content7daysPntCwOrdNum = r['content7daysPntCwOrdNum']
                # 引导7日成交子单量
                content7daysCwOrdNum = r['content7daysCwOrdNum']
                # 引导7日成交商品件数
                content7daysCwOrdGoods = r['content7daysCwOrdGoods']
                # 引导7日成交金额
                content7daysCwOrdAmount = r['content7daysCwOrdAmount']
                # 引导7日成交人数
                content7daysCwOrdUsers = r['content7daysCwOrdUsers']
                # 引导15日成交父单量
                content15daysPntCwOrdNum = r['content15daysPntCwOrdNum']
                # 引导15日成交子单量
                content15daysCwOrdNum = r['content15daysCwOrdNum']
                # 引导15日成交商品件数
                content15daysCwOrdgoods = r['content15daysCwOrdgoods']
                # 引导15日成交金额
                content15daysCwOrdAmount = r['content15daysCwOrdAmount']
                # 引导15日成交人数
                content15daysCwOrdUsers = r['content15daysCwOrdUsers']
                ws.append([
                    content_id, content_main_title, liveBroadcastWay, liveStartTm, liveEndTm, dt, pv, uv, liveLikeCnt,
                    liveLikeUserQtty, explainreplyCnt, explainreplyUserQtty, shareCnt, shareUserQtty, anchorFollowCnt,
                    anchorFollowUserQtty, skuPv, skuUv, contentCartSkuAmount, contentCartUv, shopPv, shopUv, avgStmRt,
                    content1DayPntCwOrdNum, content1DayCwOrdNum, content1DayCwOrdGoods, content1DayCwOrdAmount,
                    content1DayCwOrdUsers, content7daysPntCwOrdNum, content7daysCwOrdNum, content7daysCwOrdGoods,
                    content7daysCwOrdAmount, content7daysCwOrdUsers, content15daysPntCwOrdNum, content15daysCwOrdNum,
                    content15daysCwOrdgoods, content15daysCwOrdAmount, content15daysCwOrdUsers
                ])
    wb.save(rf"./data/jd_live_08_15.xlsx")


if __name__ == '__main__':
    get_data()
