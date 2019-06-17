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
        self.path = "/api/geek-dmp-api/member/category"
        print("----------开始测试----------")


    #客户价值接口
    def test_customerValue(self):
        self.url = self.host + self.path
        data = {"tagType":"CustomerInfo"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        # print(response.json()[0]['biType'])
        assert response.json()[0]['biType'] != "NULL"

    #销售数据接口
    def test_salesData(self):
        self.url = self.host + self.path
        data = {"tagType":"Marketing"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        # print(response.json()[0]['biType'])
        assert response.json()[0]['biType'] != "NULL"

    #营销数据接口
    def test_marketingData(self):
        self.url = self.host + self.path
        data = {"tagType":"Operation"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        # print(response.json()[0]['biType'])
        assert response.json()[0]['biType'] != "NULL"

    #基础资料接口
    def test_basicData(self):
        self.url = self.host + self.path
        data = {"tagType":"BasicsInfo"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        # print(response.json()[0]['biType'])
        assert response.json()[0]['biType'] != "NULL"

    #互联网数据接口
    def test_internetData(self):
        self.url = self.host + self.path
        data = {"tagType":"Internet"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        # print(response.json()[0]['biType'])
        assert response.json()[0]['biType'] != "NULL"


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()