import time
from pyhermit import Hermit

hm = Hermit('192.168.20.183:9999')

# # 每隔0.1秒监视一次
# while not hm._is_clickable('text', '微信红包'):
#     time.sleep(0.1)
#
# hm.click_text('微信红包')
# # 模拟器配置低，打开红包过程略慢，需要等待1秒钟，才能再开。
# hm.click_desc('开', 1)


hm.click_text('京东', 1)
# hm.shell_tap(78, 607)
# time.sleep(1)
# hm.input('id', 'com.tencent.mm:id/f3x', 'v2ex')
# hm.click_id('com.tencent.mm:id/b3b', 1)
# # hm.click_id('com.tencent.mm:id/knu', 1)
# time.sleep(5)  # 等待搜索结果
# hm.swipe_up(5)
