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
        self.path01 = "/api/geek-dmp-api/common/provinces"
        self.path02 = "/api/icem-crowd/seller/tag/value/extend"
        print("----------开始测试----------")


    #以场圈人-地理位置接口
    def test_fieldCircleProvinces(self):
        self.url = self.host + self.path01
        data = {}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #互动行为接口
    def test_platformList(self):
        self.url = self.host + self.path02
        data = {"tag":"MarketingChannel","pid":28}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()