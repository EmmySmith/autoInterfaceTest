#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
from common.public import *
import random

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.random = random.randint(1000,99999)
        self.path = "/api/icem-crowd/custom/tag/modify"
        print("----------开始测试----------")


    #添加自定义标签接口
    def test_getLabel(self):
        self.url = self.host + self.path
        self.name = "auto" + str(self.random)
        data = {"name":self.name,"tagDescribe":"测试添加"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()