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
        self.path = "/api/icem-resource/coupon/export?couponId=21&&fileType=csv&&number=4"
        print("----------开始测试----------")


    #导出优惠券文件接口
    def test_exportCouponFile(self):
        self.url = self.host + self.path
        # data = {"id":"22"}
        print(self.url)
        response = requests.get(url=self.url, headers=self.headers)
        print (response.text)
        # assert response.json()['error'] == 0
        assert("券码", response.text)


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()