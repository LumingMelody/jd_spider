import json

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import base64
import numpy as np
import cv2
import random
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
# 无可视化界面操作
options.add_argument('--headless')
options.add_argument('--dissable-gpu')
# 实现规避检测

options.add_experimental_option('excludeSwitches', ['enable-outomation'])


class Run(object):
    def __init__(self):
        # 账号和密码区块
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)
        self.driver.get(
            'https://jlive.jd.com/user/login'
        )
        self.driver.implicitly_wait(10)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[2]/iframe'))
        self.driver.find_element(By.XPATH, '//*[@id="loginname"]').send_keys("18662337940")
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="nloginpwd"]').send_keys("fd160406.")
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="paipaiLoginSubmit"]').click()
        time.sleep(1)

        # 登陆区块
        self.slider()
        # # 商品搜索，二次验证登陆
        # self.search()
        cookies = self.driver.get_cookies()
        # print(cookies)
        cookie = ''
        for i in cookies:
            if i['name'] == '__jdu' or i['name'] == '__jdv' or i['name'] == '__jda' or i['name'] == '__jdc' or i['name'] == '__jdb':
                c = i['name'] + '=' + i['value'] + ';'
                cookie += c
        print(cookie)
        # print(cookies)
        with open("cookies.txt", "w") as f:
            json.dump(cookie, f)
        # with open("cookies.txt", "r") as f:
        #     cookies = json.load(f)
        # for cookie in cookies:
        #     self.driver.add_cookie(cookie)
        # self.driver.get('https://www.jd.com')
        # time.sleep(2)
        # print(self.driver.title)
        # time.sleep(1)
        self.driver.quit()

    def slider(self):
        """
        验证码登陆
        :return:
        """
        block = self.driver.find_element(
            By.XPATH, '//*[@id="JDJRV-wrap-paipaiLoginSubmit"]/div/div/div/div[1]/div[2]/div[2]/img').get_attribute("src")
        img = self.driver.find_element(
            By.XPATH,
            '//*[@id="JDJRV-wrap-paipaiLoginSubmit"]/div/div/div/div[1]/div[2]/div[1]/img').get_attribute('src')
        block_ele = self.driver.find_element(By.XPATH, '//*[@id="JDJRV-wrap-paipaiLoginSubmit"]/div/div/div/div[1]/div[2]/div[2]/img')
        act = ActionChains(self.driver)
        act.click_and_hold(block_ele).perform()
        for i in self.offer(self.img_test(img, block)):
            act.move_by_offset(i, random.randrange(1, 3))
        act.release().perform()
        time.sleep(2)

        self.search()

    def search(self):
        """
        商品搜索操作
        :return:
        """

        # self.driver.find_element(By.CSS_SELECTOR,'#key').send_keys("净水器")
        # self.driver.find_element(By.CSS_SELECTOR,'.search-m .button').click()
        # time.sleep(2)
        # with open("京东.html","w",encoding="utf-8") as f:
        #     f.write(self.driver.page_source)

    def offer(self, offset):
        """
        处理滑块轨迹
        :param offset:
        :return:
        """

        v, current = 0, 0
        mid = offset * 3 / 5
        tracks = []
        t = 0.6
        while current < offset:
            if current < round(mid):
                a = 2
            else:
                a = -3
            s = v * t + 0.5 * a * (t ** 2)
            current += s
            v = v + a * t
            tracks.append(round(s))
        return tracks

    def img_test(self, x, y):
        """
        缺口坐标处理区块
        :param x:
        :param y:
        :return:
        """

        x = base64.b64decode(x.split(",")[-1])
        img_array = np.frombuffer(x, np.uint8)
        img = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)
        y = base64.b64decode(y.split(",")[-1])
        y = np.frombuffer(y, np.uint8)
        template = cv2.imdecode(y, cv2.COLOR_RGB2BGR)
        res = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)
        value = cv2.minMaxLoc(res)[2][0]
        distance = value * 278 / 360
        return distance


if __name__ == "__main__":
    Run()

