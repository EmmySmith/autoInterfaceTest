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
        self.path = "/api/icem-crowd/crowds?page=0&size=20&sort=createTime,desc"
        print("----------开始测试----------")


    #自定义人群列表接口
    def test_getLabel(self):
        self.url = self.host + self.path
        data = {"merchantId":"1000","type":"USER_DEFINED"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()