# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/17 18:44
@Auth ： 蔍鸣
@File ：phone_test.py
@IDE ：PyCharm
@Motto:拔丝kite博
"""

from twilio.rest import Client  # 先导入

# sid和token都是在twilio网站的个人设置中看到的
account_sid = 'ACb68faebb9cfefbbbd54a3f5890339b21'
auth_token = '793120a13bdc9744f76b2bb61e80e3b8'
# 实例化
client = Client(account_sid, auth_token)


# 16238886939
# 开始发短信
def send_msg(message):
    u'自定义短信内容message'
    msg = client.messages.create(
        to='+8613222271819',  # 要给谁发短信, 必须带区号, 中国要加上+86
        from_='+16238886939',  # 你自己twilio网站申请的手机号码, 必须带上+号
        body=message  # 你的短信内容
    )


# 开始打电话
def call_num(number):
    u'自定义打电话的号码'
    call = client.calls.create(
        to='+86' + number,  # 要给谁打电话, 必须带区号, 中国要加上+86
        from_='+16238886939',  # 你自己twilio网站申请的手机号码, 必须带上+号
        url="http://demo.twilio.com/docs/voice.xml"  # 要播放的mp3
    )


if __name__ == '__main__':
    # call_num(str(13222271819))
    send_msg('伤心')
