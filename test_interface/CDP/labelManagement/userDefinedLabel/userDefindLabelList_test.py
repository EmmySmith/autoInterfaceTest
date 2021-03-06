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
        self.path = "/api/icem-crowd/custom/tags?page=0&size=20&sort=createTime,desc"
        print("----------开始测试----------")


    #客户列表接口
    def test_getLabel(self):
        '''客户列表接口'''
        self.url = self.host + self.path
        data = {}
        print(self.url)
        print(data)
        print(self.headers)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()