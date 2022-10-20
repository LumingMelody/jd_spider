# client_id 为官网获取的AK， client_secret 为官网获取的SK
import base64

import requests
from aip import AipImageProcess

# """ 你的 APPID AK SK """
APP_ID = '26587421'
API_KEY = 'huHVvsGOS3G2i0TZBflCRzkk'
SECRET_KEY = 'KBMSkyFh5k5YAUId9SPk0mtykmDMky7f'

# client = AipImageProcess(APP_ID, API_KEY, SECRET_KEY)
# f = open('伊利.png', 'rb')
# img = base64.b64encode(f.read())
# data = client.imageDefinitionEnhance(img)
# print(data)

host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=huHVvsGOS3G2i0TZBflCRzkk&client_secret=KBMSkyFh5k5YAUId9SPk0mtykmDMky7f'
response = requests.get(host)
if response:
    print(response.json())
access_token = response.json()['access_token']
print(access_token)

'''
图像清晰度增强
'''
request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/image_definition_enhance"
# 二进制方式打开图片文件
f = open('1.png', 'rb')
img = base64.b64encode(f.read())

params = {"image": img}
request_url = request_url + "?access_token=" + str(access_token)
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json()['image'])

imgdata = base64.b64decode(response.json()['image'])
file = open('2.png', 'wb')
file.write(imgdata)
file.close()

