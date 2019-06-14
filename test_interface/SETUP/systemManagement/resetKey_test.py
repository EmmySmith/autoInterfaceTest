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
        self.path = "/api/icem-resource/configure/renew/secretKey"
        print("----------开始测试----------")


    #重置优惠券密钥接口
    def test_resetKey(self):
        self.url = self.host + self.path
        data = {}
        print(self.url)
        print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()