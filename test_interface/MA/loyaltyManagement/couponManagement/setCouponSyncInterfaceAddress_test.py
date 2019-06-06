#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
from common.public import *

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-resource/configure/set/couponSyncUrl"
        print("----------开始测试----------")


    #设置优惠券同步接口地址接口
    def test_setCouponSyncInterfaceAddress(self):
        self.url = self.host + self.path
        data = {"couponSyncUrl": "http://www.baidu.com"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()