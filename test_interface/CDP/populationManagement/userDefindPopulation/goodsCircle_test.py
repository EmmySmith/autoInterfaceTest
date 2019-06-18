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
        self.path01 = "/api/geek-dmp-api/goods/attributes"
        self.path02 = "/api/geek-dmp-api/platform/list"
        print("----------开始测试----------")


    #标签分类接口
    def test_goodsCircle(self):
        self.url = self.host + self.path01
        data = {}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #属性参数接口
    def test_platformList(self):
        self.url = self.host + self.path02
        data = {}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()