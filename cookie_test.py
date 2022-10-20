# # from urllib import request
# # from http import cookiejar
# #
# # if __name__ == '__main__':
# #     # 声明一个CookieJar对象实例来保存cookie
# #     cookie = cookiejar.CookieJar()
# #     # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
# #     handler = request.HTTPCookieProcessor(cookie)
# #     # 通过CookieHandler创建opener
# #     opener = request.build_opener(handler)
# #     # 此处的open方法打开网页
# #     response = opener.open('http://www.jd.com')
# #     # 打印cookie信息
# #     for item in cookie:
# #         print('Name = %s' % item.name)
# #         print('Value = %s' % item.value)
# import json
#
# from selenium import webdriver
# import time
# from selenium.webdriver import ChromeOptions
#
# options = ChromeOptions()
# # 无可视化界面操作
# options.add_argument('--headless')
# options.add_argument('--dissable-gpu')
# # 实现规避检测
#
# options.add_experimental_option('excludeSwitches', ['enable-outomation'])
#
# driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)
#
# driver.get('http://www.jd.com')
# time.sleep(1)
#
# cookies = driver.get_cookies()
# # print(type(cookies))
# cookie = ''
# for i in cookies:
#     print(type(i))
#     c = i['name'] + '=' + i['value'] + ';'
#     cookie += c
#
# print(cookie)
# driver.quit()
import json

with open(r'./cookies.txt', 'r') as f:
    cookies = json.load(f)
    for cookie in cookies:
        print(cookie)

