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
        # self.host = host_dev
        self.path = "/api/icem-resource/coupon/listForActivity?page=1&pageSize=10"
        print("----------开始测试----------")


    #活动-获取优惠券接口
    def test_activityGetCoupons(self):
        self.url = self.host + self.path
        data = {}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()