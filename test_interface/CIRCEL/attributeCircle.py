#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
from common.public import *

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # 根据类别获取客户标签接口
        self.headers = headers
        self.host = host
        self.path = "/api/icem-crowd/seller/tag/get"
        print("----------开始测试----------")


    #基础标签-预测&特色接口
    def test_Category_23(self):
        self.url = self.host + self.path
        data = {"id":23}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #基础信息接口
    def test_Category_8(self):
        self.url = self.host + self.path
        data = {"id":8}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #客户关系接口
    def test_Category_3(self):
        self.url = self.host + self.path
        data = {"id":3}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #频率接口
    def test_Category_4(self):
        self.url = self.host + self.path
        data = {"id":4}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #购买接口
    def test_Category_5(self):
        self.url = self.host + self.path
        data = {"id":5}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #分享行为接口
    def test_Category_6(self):
        self.url = self.host + self.path
        data = {"id":6}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #消费习惯接口
    def test_Category_7(self):
        self.url = self.host + self.path
        data = {"id":7}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #自定义标签接口
    def test_Category_9(self):
        self.url = self.host + self.path
        data = {"id":9}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #商品圈人接口
    def test_Category_11(self):
        self.url = self.host + self.path
        data = {"id":11}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #消费渠道接口
    def test_Category_13(self):
        self.url = self.host + self.path
        data = {"id":13}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #地理位置接口
    def test_Category_14(self):
        self.url = self.host + self.path
        data = {"id":14}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #互动行为接口
    def test_Category_15(self):
        self.url = self.host + self.path
        data = {"id":15}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #自定义人群接口
    def test_Category_20(self):
        self.url = self.host + self.path
        data = {"id":20}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #上传人群接口
    def test_Category_22(self):
        self.url = self.host + self.path
        data = {"id":22}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0



    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()