#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
from common.public import *
from parameterized import parameterized

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-log/operation/logs?page=0&size=20"
        print("----------开始测试----------")

    # @parameterized.expand(input=create_baosundan.dates())
    #查询系统日志接口
    def test_system_log(self):
        self.url = self.host + self.path
        data = {"page":0,"size":20,"endCreateTime":""}
        print(self.url)
        print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['content'] != "null"


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()