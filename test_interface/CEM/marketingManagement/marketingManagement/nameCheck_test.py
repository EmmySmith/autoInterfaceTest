#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json,time,random
from common.public import *

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-activity/market/check/activity/name"
        self.random = random.randint(1000,99999)
        print("----------开始测试----------")


    #营销活动名称检查接口
    def test_nameCheck_flase(self):
        '''已存在的活动名称'''
        self.url = self.host + self.path
        data = {"name":"自动化名称"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 4299
        assert response.json()['message'] == "活动名称已存在！！！"


    def test_nameCheck_true(self):
        '''可用的活动名称'''
        self.url = self.host + self.path
        self.name = "自动化名称" + str(self.random)
        data = {"name":self.name}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()