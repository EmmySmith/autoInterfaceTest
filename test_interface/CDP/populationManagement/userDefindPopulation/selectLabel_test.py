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
        self.path = "/api/icem-crowd/seller/tag/get/value"
        print("----------开始测试----------")


    #属性圈人-基础信息接口
    def test_selectBaseInfo(self):
        self.url = self.host + self.path
        data = {"id":92,"tag":"Gender"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #属性圈人-基础标签-预测&特色
    def test_selectBaseLabel(self):
        self.url = self.host + self.path
        data = {"id":99,"tag":"Occupation"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #属性圈人-客户关系-CustomerIntimacy
    def test_selectCustomerRelationship_CustomerIntimacy(self):
        self.url = self.host + self.path
        data = {"id":1,"tag":"CustomerIntimacy"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #属性圈人-客户关系-PointsExchangeProduct
    def test_selectCustomerRelationshipPointsExchangeProduct(self):
        self.url = self.host + self.path
        data = {"id":17,"tag":"PointsExchangeProduct"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #属性圈人-频率
    def test_selectFrequency(self):
        self.url = self.host + self.path
        data = {"id":39,"tag":"BuyCountLevel"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #属性圈人-购买
    def test_selectBuy(self):
        self.url = self.host + self.path
        data = {"id":50,"tag":"LastOrderProduct"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #属性圈人-分享行为
    def test_selectSharingBehavior(self):
        self.url = self.host + self.path
        data = {"id":59,"tag":"ShareCount"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #属性圈人-消费习惯
    def test_selectConsumptionHabits(self):
        self.url = self.host + self.path
        data = {"id":64,"tag":"FrequentTime"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0



    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()