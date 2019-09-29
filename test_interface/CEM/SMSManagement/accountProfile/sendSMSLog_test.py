#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json,time,random
from common.public import *
from mysqlHandle.common_mysql import *

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-sms/sms/log/list?page=1&size=10"
        print("----------开始测试----------")


    #发送短信接口
    def test_sendSMSLog(self):
        '''发送短信接口'''
        self.url = self.host + self.path
        data = {}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()