# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/12 17:03
@Auth ： 蔍鸣
@File ：hot_answer.py
@IDE ：PyCharm
@Motto:拔丝kite博
"""
import json
import re
from pymysql import *

conn = connect(host='rm-uf664y8bsz73u37odio.mysql.rds.aliyuncs.com', port=3306, database='dts_prod', user='luming',
               password='Luming1314', charset='utf8')
cursor = conn.cursor()


# mitmdump -s script.py -p 9090
def response(flow):
    # 提取请求的 url 地址
    request_url = flow.request.url
    print(request_url)

    if bool(re.search(r"/api/feeds/get_feeds_list", request_url)):
        print("request_url >>> ", request_url)
        response_body = flow.response.text
        response_url = flow.request.url

        print("response_url >>> ", response_url)
        data = json.loads(response_body)
        ware_infos = data.get("data")
        if ware_infos is not None:
            for ware_info in ware_infos['list']:
                info = {}
                info['title'] = ware_info['title']
                # info["pv_num"] = ware_info['pvNum']
                # info['title'] = ware_info['title']
                # info["article_id"] = ware_info['articleId']
                # info["index_img"] = ware_info['indexImage']
                # # info["product_sku"] = ware_info['productList'][0]['sku']
                # # info["publishDate"] = ware_info['publishDate']
                # # info["replyCount"] = ware_info['replyFloor']['replyCount']
                # if 'playInfo' in ware_info.keys():
                #     info['video_url'] = ware_info['playInfo']['videoUrl']
                #     info['video_img'] = ware_info['playInfo']['videoImg']
                # else:
                #     info['video_url'] = ''
                #     info['video_img'] = ''
                # # jd_app.insert(info)
                table_name = "baby_tree"
                cols = ", ".join('`{}`'.format(k) for k in info.keys())
                placeholders = ', '.join('%({})s'.format(k) for k in info.keys())
                insert_sql = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
                cursor.execute(insert_sql, info)
            conn.commit()
