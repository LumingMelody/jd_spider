import json
import time
import re
from pymysql import *

# MONGO_URL = 'mongodb://luming:123456@localhost:27017/?authSource=luming'
# client = MongoClient(MONGO_URL)
# db = client['luming']
# db.authenticate('luming', '123456')
# jd_app = db['jd_app']
# jd_keyword = db['jd_keyword']

# get_keyword = Blueprint('get_keyword', strict_slashes=True)

conn = connect(host='', port=3306, database='dts_prod', user='luming',
               password='', charset='utf8')
cursor = conn.cursor()


# discSearchExecuteNew
# mitmdump -s script.py -p 9090
def response(flow):
    # 提取请求的 url 地址
    request_url = flow.request.url
    print(request_url)
    # 通过 jd 字符串，过滤出 京东APP 的请求和返回数据
    if bool(re.search(r"getRecommendNewFeedsLis", request_url)):
        print("request_url >>> ", request_url)
        response_body = flow.response.text
        response_url = flow.request.url

        print("response_url >>> ", response_url)
        data = json.loads(response_body)
        ware_infos = data.get("data")
        if ware_infos is not None:
            for ware_info in ware_infos['list']:
                info = {}
                info['author_name'] = ware_info['authorName']
                info["pv_num"] = ware_info['pvNum']
                info['title'] = ware_info['title']
                info["article_id"] = ware_info['articleId']
                info["index_img"] = ware_info['indexImage']
                # info["product_sku"] = ware_info['productList'][0]['sku']
                # info["publishDate"] = ware_info['publishDate']
                # info["replyCount"] = ware_info['replyFloor']['replyCount']
                if 'playInfo' in ware_info.keys():
                    info['video_url'] = ware_info['playInfo']['videoUrl']
                    info['video_img'] = ware_info['playInfo']['videoImg']
                else:
                    info['video_url'] = ''
                    info['video_img'] = ''
                # jd_app.insert(info)
                table_name = "jd_app"
                cols = ", ".join('`{}`'.format(k) for k in info.keys())
                placeholders = ', '.join('%({})s'.format(k) for k in info.keys())
                insert_sql = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
                cursor.execute(insert_sql, info)
            conn.commit()
    # discSearchExecuteNew
    elif bool(re.search(r"discSearchExecuteNew", request_url)):
        print("request_url >>> ", request_url)
        response_body = flow.response.text
        response_url = flow.request.url
        print("response_url >>> ", response_url)
        post_p = flow.request.urlencoded_form
        keyword = str(post_p).split(':')[-1].split('}')[0]
        data = json.loads(response_body)
        ware_infos = data.get("result")
        if ware_infos is not None:
            for ware_info in ware_infos['contentList']:
                info = {}
                if 'content' not in ware_info.keys():
                    info['author_name'] = ware_info['authorName']
                    info["author_id"] = ware_info['authorId']
                    info["author_pic"] = ware_info['authorPic']
                    info['title'] = ware_info['title']
                    info['page_view'] = ware_info['pageView']
                    info['skus'] = ware_info['skus']
                    publishTime = ware_info['publishTime']
                    publishTime = int(publishTime) / 1000
                    timeArray = time.localtime(publishTime)
                    info["post_time"] = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                    video_id = ware_info['id']
                    info["video_url"] = f'https://h5.m.jd.com/active/faxian/video/index.html?id={video_id}'
                    info['key_word'] = keyword
                    # jd_keyword.insert(info)
                    table_name = "jd_keyword"
                    cols = ", ".join('`{}`'.format(k) for k in info.keys())
                    placeholders = ', '.join('%({})s'.format(k) for k in info.keys())
                    insert_sql = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
                    cursor.execute(insert_sql, info)
            conn.commit()
        # discSearchExecute
    # 
    #     # discSearchExecute

    # elif bool(re.search(r"discSearchExecute", request_url)):
    #     print("request_url >>> ", request_url)
    #     response_body = flow.response.text
    #     response_url: object = flow.request.url
    #     print("response_url >>> ", response_url)
    #     post_p = flow.request.urlencoded_form
    #     keyword = str(post_p).split(':')[-1].split('}')[0]
    #     data = json.loads(response_body)
    #     ware_infos = data.get("searchContext")
    #     for ware_info in ware_infos:
    #         info = {}
    #         info['author_id'] = ware_info['authorId']
    #         info['title'] = ware_info['title']
    #         info["summary"] = ware_info['summary']
    #         info["index_img"] = ware_info['indexImage']
    #         info['page_view'] = ware_info['pageView']
    #         info['sku'] = ware_info['sku']
    #         info['j_id'] = ware_info['id']
    #         info['key_word'] = keyword
    #         table_name = "jd_find_goods"
    #         cols = ", ".join('`{}`'.format(k) for k in info.keys())
    #         placeholders = ', '.join('%({})s'.format(k) for k in info.keys())
    #         insert_sql = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
    #         cursor.execute(insert_sql, info)
    #     conn.commit()
