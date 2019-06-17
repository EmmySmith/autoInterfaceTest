#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
from common.public import *
from mysqlHandle.common_mysql import *

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/geek-dmp-api/member/info"
        self.sql = "SELECT id from t_customer_list ORDER BY id DESC LIMIT 1;"
        self.dbname = "geek_dmp_api"
        print("----------开始测试----------")


    #firstTrading接口
    def test_firstTrading(self):
        self.url = self.host + self.path
        self.customerId = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))
        data = {"merchantId":"1000","merchantMemberId":self.customerId,"biType":"firstTrading","categoryId":45}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #lastTrading接口
    def test_lastTrading(self):
        self.url = self.host + self.path
        self.customerId = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))
        data = {"merchantId":"1000","merchantMemberId":self.customerId,"biType":"lastTrading","categoryId":46}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #valueConsumptionFrequency接口
    def valueConsumptionFrequency(self):
        self.url = self.host + self.path
        self.customerId = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))
        print(self.customerId)
        data = {"merchantId":"1000","merchantMemberId":25,"biType":"valueConsumptionFrequency","categoryId":47}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #valueLifeCycle接口
    def test_valueLifeCycle(self):
        self.url = self.host + self.path
        self.customerId = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))
        data = {"merchantId":"1000","merchantMemberId":self.customerId,"biType":"valueLifeCycle","categoryId":49}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #valueUnitPrice接口
    def test_valueUnitPrice(self):
        self.url = self.host + self.path
        self.customerId = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))
        data = {"merchantId":"1000","merchantMemberId":self.customerId,"biType":"valueUnitPrice","categoryId":50}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #valueLevelNew接口
    def test_valueLevelNew(self):
        self.url = self.host + self.path
        self.customerId = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))
        data = {"merchantId":"1000","merchantMemberId":self.customerId,"biType":"valueLevelNew","categoryId":51}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #valueLevelOld接口
    def test_valueLevelOld(self):
        self.url = self.host + self.path
        self.customerId = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))
        data = {"merchantId":"1000","merchantMemberId":self.customerId,"biType":"valueLevelOld","categoryId":52}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #unifiedInfo接口
    def test_unifiedInfo(self):
        self.url = self.host + self.path
        self.customerId = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))
        data = {"merchantId":"1000","merchantMemberId":self.customerId,"biType":"unifiedInfo","categoryId":44}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0



    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()