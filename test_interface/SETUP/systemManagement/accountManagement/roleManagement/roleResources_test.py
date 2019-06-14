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
        self.path = "/api/icem-system/system/resources"
        print("----------开始测试----------")


    #角色资源页面接口
    def test_role_resources(self):
        self.url = self.host + self.path
        data = {}
        print(self.url)
        print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        # assert response.json()['type'] == "NO"


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()