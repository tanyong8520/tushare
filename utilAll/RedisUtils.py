# -*- coding: utf-8 -*-
import redis

class RedisUtils:
    _HOST = '127.0.0.1'
    _POST = '6379'
    pool = None

    def __init__(self):
        self.pool = redis.ConnectionPool(host=self._HOST, port=self._POST)
        self.channel = 'test'

    def getConnect(self):
        return redis.Redis(connection_pool=self.pool)

    def publish(self, msg):  # 定义发布方法
        self.getConnect().publish(self.channel, msg)
        return True

    def subscribe(self):  # 定义订阅方法
        pub = self.getConnect().pubsub()
        pub.subscribe(self.channel)
        pub.parse_response()
        return pub


if __name__ == '__main__':
    redis = RedisUtils()
    redis