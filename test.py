# # # # import plotly.express as px
# # # #
# # # # df = px.data.gapminder()
# # # # fig = px.scatter(
# # # #     df,
# # # #     x="gdpPercap",
# # # #     y="lifeExp",
# # # #     animation_frame="year",
# # # #     size="pop",
# # # #     color="continent",
# # # #     hover_name="country",
# # # #     log_x=True,
# # # #     size_max=55,
# # # #     range_x=[100, 100000],
# # # #     range_y=[25, 90],
# # # #     #   color_continuous_scale=px.colors.sequential.Emrld
# # # # )
# # # # fig.update_layout(width=1000,
# # # #                   height=800,
# # # #                   xaxis_showgrid=False,
# # # #                   yaxis_showgrid=False,
# # # #                   paper_bgcolor='rgba(0,0,0,0)',
# # # #                   plot_bgcolor='rgba(0,0,0,0)')
# # # # fig.show()
# # #
# # #
# # # # import plotly.express as px
# # # # from vega_datasets import data
# # # # df = data.disasters()
# # # # df = df[df.Year > 1990]
# # # # fig = px.bar(df,
# # # #              y="Entity",
# # # #              x="Deaths",
# # # #              animation_frame="Year",
# # # #              orientation='h',
# # # #              range_x=[0, df.Deaths.max()],
# # # #              color="Entity")
# # # # # improve aesthetics (size, grids etc.)
# # # # fig.update_layout(width=1000,
# # # #                   height=800,
# # # #                   xaxis_showgrid=False,
# # # #                   yaxis_showgrid=False,
# # # #                   paper_bgcolor='rgba(0,0,0,0)',
# # # #                   plot_bgcolor='rgba(0,0,0,0)',
# # # #                   title_text='Evolution of Natural Disasters',
# # # #                   showlegend=False)
# # # # fig.update_xaxes(title_text='Number of Deaths')
# # # # fig.update_yaxes(title_text='')
# # # # fig.show()
# # #
# # # # from pymysql import *
# # # #
# # # # conn = connect(host='rm-uf664y8bsz73u37odio.mysql.rds.aliyuncs.com', port=3306, database='jd_notes', user='luming',
# # # #                password='Luming1314', charset='utf8')
# # # # cursor = conn.cursor()
# # # #
# # # # info = { 'id': 1, 'author_name': "大金小金", 'author_id': "740936", 'author_pic':
# # # # "https://storage.360buyimg.com/i.imageUpload/6a645f5679715050696f6955486c6431363339313130313339353933_big.jpg",
# # # # 'title': "生而强悍的手机iQOO7", 'page_view': 31863, 'skus': "10026522049515", 'post_time': "2021-08-03 17:37:25",
# # # # 'video_url': "https://h5.m.jd.com/active/faxian/video/index.html?id=266943630", 'keyword': 'iqoo', } table_name =
# # # # "jd_keyword" cols = ", ".join('`{}`'.format(k) for k in info.keys()) placeholders = ', '.join('%({})s'.format(k)
# # # # for k in info.keys()) insert_sql = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})" cursor.execute(
# # # # insert_sql, info) conn.commit()
# # #
# # # #
# # # # from PIL import Image
# # # # import matplotlib.pyplot as plt
# # # #
# # # #
# # # # def reshape_image(image, size):
# # # #     iw, ih = image.size
# # # #     w, h = size
# # # #     scale = min(w / iw, h / ih)
# # # #     nw = int(iw * scale)
# # # #     nh = int(ih * scale)
# # # #
# # # #     image = image.resize((nw, nh), Image.BICUBIC)
# # # #     new_image = Image.new('RGB', size, (128, 128, 128))
# # # #     new_image.paste(image, ((w - nw) // 2, (h - nh) // 2))
# # # #     return new_image
# # # #
# # # #
# # # # import numpy as np
# # # import cv2
# # # import cv2 as cv
# # #
# # #
# # # # import os
# # # # import matplotlib.pyplot as plt
# # # #
# # # #
# # # # def remove_the_blackborder(image):
# # # #     image = cv2.imread(image)  # 读取图片
# # # #     img = cv2.medianBlur(image, 5)  # 中值滤波，去除黑色边际中可能含有的噪声干扰
# # # #     b = cv2.threshold(img, 3, 255, cv2.THRESH_BINARY)  # 调整裁剪效果
# # # #     binary_image = b[1]  # 二值图--具有三通道
# # # #     binary_image = cv2.cvtColor(binary_image, cv2.COLOR_BGR2GRAY)
# # # #     # print(binary_image.shape)     #改为单通道
# # # #
# # # #     edges_y, edges_x = np.where(binary_image == 255)  ##h, w
# # # #     bottom = min(edges_y)
# # # #     top = max(edges_y)
# # # #     height = top - bottom
# # # #
# # # #     left = min(edges_x)
# # # #     right = max(edges_x)
# # # #     height = top - bottom
# # # #     width = right - left
# # # #
# # # #     res_image = image[bottom:bottom + height, left:left + width]
# # # #
# # # #     plt.figure()
# # # #     plt.subplot(1, 2, 1)
# # # #     plt.imshow(image)
# # # #     plt.subplot(1, 2, 2)
# # # #     plt.imshow(res_image)
# # # #     # plt.savefig(os.path.join("res_combine.jpg"))
# # # #     plt.show()
# # # #     return res_image
# # # #
# # # #
# # # # if __name__ == '__main__':
# # # #     image = Image.open(r'./img.png')
# # # #     print(image.size)
# # # #     plt.figure(1)
# # # #     plt.imshow(image)
# # # #     img = reshape_image(image, [750, 500])
# # # #     print(img.size)
# # # #     plt.figure(2)
# # # #     plt.imshow(img)
# # # #     # plt.show()
# # # #     img.save('./img1.png')
# # # # source_path = "./伊利.png"
# # # # save_path = "out"
# # # # if not os.path.exists(save_path):
# # # #     os.mkdir(save_path)
# # # #
# # # # img = remove_the_blackborder(source_path)
# # # # cv2.imwrite(os.path.join(save_path, "res_0923.jpg"), img)
# # #
# # # # from skimage import transform, data, io
# # # # import matplotlib.pyplot as plt
# # # #
# # # # # from PIL import Image
# # # #
# # # # img = io.imread('./WechatIMG2939.jpg')
# # # # dst = transform.resize(img, (500, 750))
# # # #
# # # # io.imsave('./1.png', dst)
# # #
# # #
# # # def resize_size(image, scale_size):
# # #     #     top,bottom,left,right = (0,0,0,0)
# # #     h, w = image.shape[0], image.shape[1]
# # #     scale = max(h, w) / scale_size  # 根据边框最大值计算比例
# # #     new_w, new_h = int(w / scale), int(h / scale)
# # #     resize_img = cv2.resize(image, (new_w, new_h))
# # #     if new_w % 2 != 0 and new_h % 2 == 0:  # 填充至scale_size * scale_size中
# # #         top, bottom, left, right = (scale_size - new_h) / 2, (scale_size - new_h) / 2, (scale_size - new_w) / 2 + 1, (
# # #                 scale_size - new_w) / 2
# # #     elif new_h % 2 != 0 and new_w % 2 == 0:
# # #         top, bottom, left, right = (scale_size - new_h) / 2 + 1, (scale_size - new_h) / 2, (scale_size - new_w) / 2, (
# # #                 scale_size - new_w) / 2
# # #     elif new_h % 2 == 0 and new_w % 2 == 0:
# # #         top, bottom, left, right = (scale_size - new_h) / 2, (scale_size - new_h) / 2, (scale_size - new_w) / 2, (
# # #                 scale_size - new_w) / 2
# # #     else:
# # #         top, bottom, left, right = (scale_size - new_h) / 2 + 1, (scale_size - new_h) / 2, (
# # #                 scale_size - new_w) / 2 + 1, (scale_size - new_w) / 2
# # #     pad_img = cv2.copyMakeBorder(resize_img, int(top), int(bottom), int(left), int(right), cv2.BORDER_CONSTANT,
# # #                                  value=[255, 255, 255])  # 设定图片框架
# # #     pad_img_cut = pad_img[250:500, 0:750]  # 需调整参数，以达到切图效果
# # #     return pad_img_cut
# # #
# # #
# # # if __name__ == '__main__':
# # #     image_source = cv2.imread('./WechatIMG2939.jpg')  # 读取图片
# # #     image = resize_size(image_source, 750)  # 缩放裁剪尺寸
# # #     cv2.imwrite('./2.png', image)  # 重命名并且保存
# # import os
# #
# # import pandas as pd
# # from PIL import Image
# #
# # # import warnings
# # #
# # # import requests
# #
# # # import pandas as pd
# # # from datetime import date, timedelta
# # #
# # # warnings.filterwarnings('ignore')
# # #
# # # data = pd.read_excel('D:/直播间详情页_京东美妆高端护肤旗舰店_2022-08-19_08-10-45_整场数据下载(1).xlsx',
# # #                      sheet_name='商品分析-商品明细')
# # # df = data.dropna(axis=0, how="any")
# # # df = data.dropna(subset=['商品名称'])
# # # df = data[-data['商品名称'].isin(['-', '商品名称'])]
# # # df = pd.DataFrame(book)
# # # gs = df['商品点击人数'] / df['商品曝光人数']
# # # df['商品点击率'] = gs
# # # gs1 = df['成交件数'] / df['商品点击人数']
# # # df['成交转化率'] = gs1
# # #
# # #
# # # start = date(2022, 8, 30)
# # # df['日期'] = start
# # # df.to_excel('D:/8.3011.xlsx', index=False)
# # # print("已完成表格")
# #
# #
# # # if __name__ == '__main__':
# # #     writer = pd.ExcelWriter("img.xlsx")
# # #     li_st = []
# # #     for root, dirs, files, in os.walk(r'./image'):
# # #         for file in files:
# # #             img_path = root + '/' + file
# # #             img = Image.open(img_path)
# # #             print(img)
# # # writer.save()
# #
# # import xlsxwriter
# # import os
# # import os.path
# # from PIL import Image
# # import sys
# #
# # UI_ROOT = r'./image'
# #
# # # Create an new Excel file and add a worksheet.
# # workbook = xlsxwriter.Workbook('images.xlsx')
# # worksheet = workbook.add_worksheet()
# #
# # # Widen the first column to make the text clearer.
# # worksheet.set_column('A:A', 5)
# # worksheet.set_column('B:B', 30)
# # worksheet.set_column_pixels('C:C', 200)
# #
# # # 设置第一行文字
# # red_format = workbook.add_format({'bold': True, 'font_color': 'red'})
# # red_format.set_align('center')
# # worksheet.write('A1', r'序号', red_format)
# # worksheet.write('B1', r'路径', red_format)
# # worksheet.write('C1', r'图片', red_format)
# #
# # v_format = workbook.add_format()
# # v_format.set_align('center')
# # v_format.set_align('vcenter')  # 居中格式
# #
# # row_index = 2
# # for root, dirs, files in os.walk(UI_ROOT):
# #     for file in files:
# #         img_path = root + '/' + file
# #         print(file)
# #         if 'DS_Store' not in img_path:
# #             img = Image.open(img_path)
# #
# #             row_height = img.height
# #             xscale = 0.5
# #             yscale = 0.5
# #
# #             worksheet.set_row(row_index - 1, row_height)  # 设置行高度
# #             worksheet.write('A{}'.format(row_index), row_index - 1, v_format)
# #             worksheet.write('B{}'.format(row_index), img_path, v_format)
# #             worksheet.insert_image('C{}'.format(row_index), img_path,
# #                                    {'object_position': 1, 'x_scale': xscale, 'y_scale': yscale, 'x_offset': 30})
# #
# #             row_index += 1
# #
# # workbook.close()
# #
# # import json
# #
# # dit1 = {'a': '1', 'b': '2', 'c': '3', 'd': '4'}
# #
# # # print(dit1)
# # print(dit1.values())
#
#
# # for i in range(1, 10):
# #     i += 1
# #     print(i)
#
#
# # import requests
# # import re
# #
# # # 发送 HTTP 请求获取网页内容
# # response = requests.get("https://www.jd.com/product/100008451775.html")
# # html = response.text
# #
# # # 使用正则表达式抓取商品名称
# # name_pattern = re.compile(r'<title>>(.*?)</title>')
# # name_match = name_pattern.search(html)
# # if name_match:
# #     name = name_match.group(1)
# # else:
# #     name = "Unknown"
# #
# # # 使用正则表达式抓取商品价格
# # price_pattern = re.compile(r'<span[^>]*class="p-price"[^>]*>([^<]+)</span>')
# # price_match = price_pattern.search(html)
# # if price_match:
# #     price = price_match.group(1)
# # else:
# #     price = "Unknown"
# #
# # # 打印结果
# # print(f"Product name: {name}")
# # print(f"Product price: {price}")
#
#
# # 导入所需模块
# import requests
# from bs4 import BeautifulSoup
#
# # 请求 URL 并获取页面信息
# url = "https://www.jd.com/product/100008451775.html"
# response = requests.get(url)
# html = response.content.decode("utf-8")
#
# # 使用 BeautifulSoup 解析页面
# soup = BeautifulSoup(html, "html.parser")
#
# # 找到所有的商品信息
# goods = soup.find_all("div", class_="goods-item")
#
# # 循环输出每个商品的信息
# for good in goods:
#     # 找到商品的名称并输出
#     name = good.find("div", class_="p-name").text
#     print(name)
#
#     # 找到商品的价格并输出
#     price = good.find("div", class_="p-price").text
#     print(price)
#
#     # 找到商品的图片并输出
#     img = good.find("img")
#     print(img["src"])
import random

# a = input("请输入：").upper()
# b = input("请输入：").upper()
# print(a.count(b))

#
# lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1]
# print(set(lis))

# num = int(input())
# l = list()
# n = 0
# while n < num:
#     i = int(input())
#     for x in l:
#         if x == i:
#             n += 1
#             continue
#     l.append(i)
#     n += 1
# for x in l:
#     print(x)

# count = int(input("请输入随机数个数："))
# lis = []
# for i in range(count):
#     num = random.randint(1, 500)
#     lis.append(num)
# print(lis)
# print(sorted(set(lis), reverse=True))

#
# lst = [1, 2, 3, 4, 5]
#
# print(' '.join(str(i) for i in lst))

n = int(input("请输入需要分解的数字："))

print("{} =".format(n), end=' ')
lis = []
while n > 1:
    for i in range(2, n + 1):
        if n % i == 0:
            n = int(n / i)
            if n == 1:
                print(i)
                lis.append(i)
            else:
                lis.append(i)
                print("{} *".format(i), end=' ')
            break

print(' '.join(str(i) for i in lis))