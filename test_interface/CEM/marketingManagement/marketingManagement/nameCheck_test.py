#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json,time
from common.public import *

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-activity/market/check/activity/name"
        print("----------开始测试----------")


    #营销列表接口
    def test_marketingList(self):
        self.url = self.host + self.path
        data = {"name":"自动化名称"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0



    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()