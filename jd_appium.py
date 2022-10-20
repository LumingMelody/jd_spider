import unittest
import selenium
import time
from appium import webdriver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # super().setUp()
        print('selenium version = ', selenium.__version__)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '12.0.0'
        desired_caps['deviceName'] = 'Pixel_4_XL'
        desired_caps['appPackage'] = 'com.tencent.qqlite'
        desired_caps["noReset"] = True
        desired_caps['appActivity'] = 'com.tencent.mobileqq.activity.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def testQQLogin(self):
        time.sleep(2)
        self.driver.find_element_by_id("com.tencent.qqlite:id/btn_login").click()

        time.sleep(5)
        self.driver.find_element_by_xpath('//android.widget.EditText[@content-desc="请输入QQ号码或手机或邮箱"]').send_keys(
            "2572652583")
        time.sleep(5)
        self.driver.find_element_by_id('com.tencent.qqlite:id/password').send_keys("123456789")
        time.sleep(5)
        self.driver.find_element_by_id('com.tencent.qqlite:id/login').click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()