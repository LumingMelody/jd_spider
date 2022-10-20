# -*- coding: utf-8 -*-
"""
@Time ： 2022/9/22 10:28
@Auth ： 蔍鸣
@File ：qian_chuan.py
@IDE ：PyCharm
@Motto:拔丝kite博
"""
import time
import requests
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.append(['时间', '花费', 'rio'])

cookies = {
    'd_ticket': '9113e87bdf7a31b52a11b23dd134efc5a5722',
    'n_mh': 'hEWL3pNYytHkGOY06d3FOIQS3ryMrcKB7wFjnSZcfR0',
    'sso_uid_tt': 'e139a8dea45af78c35267f69c6e8bce0',
    'sso_uid_tt_ss': 'e139a8dea45af78c35267f69c6e8bce0',
    'toutiao_sso_user': '762018d72d20f9b9aaa54c4f73fa5fcf',
    'toutiao_sso_user_ss': '762018d72d20f9b9aaa54c4f73fa5fcf',
    'sid_ucp_sso_v1': '1.0.0-KDYwYTY5Y2M5NzJkZDgyOTQzMjExODU2NzhmMzgxMDE0MzVlYTQzMmEKHgin46DIqI32ARDF-8KXBhimDCAMMNCroo0GOAhAJhoCbGYiIDc2MjAxOGQ3MmQyMGY5YjlhYWE1NGM0ZjczZmE1ZmNm',
    'ssid_ucp_sso_v1': '1.0.0-KDYwYTY5Y2M5NzJkZDgyOTQzMjExODU2NzhmMzgxMDE0MzVlYTQzMmEKHgin46DIqI32ARDF-8KXBhimDCAMMNCroo0GOAhAJhoCbGYiIDc2MjAxOGQ3MmQyMGY5YjlhYWE1NGM0ZjczZmE1ZmNm',
    'odin_tt': '8eb1810cf6fc6c40dfe68ff9427427628fb1afbcf6186f64c71313909d7c213303bb6849ce72a24fa882d68eeaafbf3e041907b73188afaff3b921d5b69d78ba',
    'sid_guard': 'dbdc93ac473af4315f85635687872e4d%7C1659944394%7C5184000%7CFri%2C+07-Oct-2022+07%3A39%3A54+GMT',
    'uid_tt': '3b9dc3e676a6cc22c2017fdd2c42b06e',
    'uid_tt_ss': '3b9dc3e676a6cc22c2017fdd2c42b06e',
    'sid_tt': 'dbdc93ac473af4315f85635687872e4d',
    'sessionid': 'dbdc93ac473af4315f85635687872e4d',
    'sessionid_ss': 'dbdc93ac473af4315f85635687872e4d',
    'sid_ucp_v1': '1.0.0-KGVhZDA4MmE1YTAzMTVmMjVhNTU2ODlkNjE2ZGZhNjM5MjMzNjFmMTgKFgin46DIqI32ARDK-8KXBhiPETgIQCYaAmhsIiBkYmRjOTNhYzQ3M2FmNDMxNWY4NTYzNTY4Nzg3MmU0ZA',
    'ssid_ucp_v1': '1.0.0-KGVhZDA4MmE1YTAzMTVmMjVhNTU2ODlkNjE2ZGZhNjM5MjMzNjFmMTgKFgin46DIqI32ARDK-8KXBhiPETgIQCYaAmhsIiBkYmRjOTNhYzQ3M2FmNDMxNWY4NTYzNTY4Nzg3MmU0ZA',
    'ttwid': '1%7COwMHNUDxLKbSsOvXm8J9i6qZ9I_mJbb9ZehSclbfoGc%7C1660117446%7Cb524a7aa45e6701a82102501062c989ff6c3b4490e4d07e78c506f21259c4dfc',
    'x-jupiter-uuid': '16638133480345564',
    'qc_tt_tag': '0',
    'csrf_session_id': '4ad6826d6c14edf168603eaf4e768f1d',
    'csrftoken': 'aREojvRa-kJYpeCkjYr8I_jaHS9V4yxm7ir8',
    'ttcid': '86b5775c50d84ac7ac8224754bc3961635',
    'tt_scid': 'CVJ6v8bZwSVpQUuTxgXfVEdpmwh59L-TyT04oRPnxvgJa7gVoeo-7AbNC22ao9VT5680',
    'msToken': 'EeqbUlmnMlSaeV-ZvAyaA2ImuwhA8kdtFDpriXANSz7U1bATQUJoUZJF5LeYZ1XU_QcTXuAgvvqi8J8H2xz5v7Yna0uj2tGbmdqAu7VOLLDtIc26Fk2V4nP2cShdkvSA',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://qianchuan.jinritemai.com',
    'Pragma': 'no-cache',
    'Referer': 'https://qianchuan.jinritemai.com/?aavid=1740674025197576&x_tt_random=1663813534628',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'X-CSRFToken': 'aREojvRa-kJYpeCkjYr8I_jaHS9V4yxm7ir8',
    'qc-auth': '2b7a6989d4508d5a39801f2abeff85b2',
    'qc-date': '1663813607360',
    'qc-key': 'ucimr6iw',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}


def get_data():
    data = '{"statsParameter":{"startTime":"2022-09-17 00:00:00","endTime":"2022-09-17 23:59:59","metrics":["stat_cost","all_order_pay_roi_7days"],"mainDimension":"advertiser_id","timeDimension":"stat_time_hour","orderField":"stat_time_hour","orderType":1,"pageParams":{"page":-1,"pageSize":500}},"downloadParameter":{"download":false,"columns":["stat_cost","all_order_pay_roi_7days"]},"marGoal":0,"campaignType":0,"userField":false,"aavid":"1740674025197576"}'
    # print(type(data))
    url = 'https://qianchuan.jinritemai.com/ad/marketing/data/api/v1/common/order_stats_data?aavid=1740674025197576&gfversion=1.0.1.499'
    response = requests.post(url, headers=headers, cookies=cookies, data=data).json()
    # print(response.json())
    result = response['data']['data']['statsDataRows']
    for r in result:
        ts = int(r['dimensions']['statTimeHour'])
        # print(type(ts))
        time_array = time.localtime(ts)
        stat_time_hour = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
        spend = r['metrics']['statCost']['value']
        roi = r['metrics']['allOrderPayRoi7Days']['value']
        ws.append([stat_time_hour, spend, roi])
    wb.save('qian_chuan.xlsx')


if __name__ == '__main__':
    get_data()
