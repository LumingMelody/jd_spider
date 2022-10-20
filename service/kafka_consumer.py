"""
@version: 1.0
@author: anne
@contact: thy.self@foxmail.com
@time: 2021/11/27 上午11:16
"""
import sys
import _thread
import json
from kafka import KafkaConsumer
from loguru import logger
from peewee import fn
from service.save import save_category


def kafka_consumer_executor():
    """
    :param platform:
    :return:
    """
    # topic_name = platform_code_en[platform]
    # consumer = KafkaConsumer('jd_category', bootstrap_servers=["106.14.217.68:9092"])
    consumer = KafkaConsumer('jd_category', bootstrap_servers=["127.0.0.1:9092"])
    # logger.info(f'当前启动topic消费者：{topic_name}')

    # pl = platform_code_query[platform]
    # max_id = pl.select(fn.MAX(pl.id).alias('max_id'))[0].max_id
    # max_id = max_id if max_id else 1
    # logger.info(f'当前已消费的最大id：{str(max_id)}')

    for msg in consumer:
        info = json.loads(str(msg.value, encoding='utf8'))
        logger.info(info)
        # max_id += 1
        # 异步insert 数据到mysql, 工单数据单句存储，异步提高速度
        _thread.start_new_thread(save_category, (info, ))


if __name__ == '__main__':
    # python3 -m src.services.kafka.kafka_consumer 1
    # kafka_consumer_executor(int(sys.argv[3]))
    kafka_consumer_executor()
