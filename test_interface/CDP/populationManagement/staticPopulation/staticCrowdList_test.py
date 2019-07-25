#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
import random
from common.public import *

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        # self.name = random.randint(1000,9000)
        self.path = "/api/icem-crowd/crowds?page=0&size=20&sort=status,desc&sort=createTime,desc"
        print("----------开始测试----------")


    #静态人群列表
    def test_staticCrowdList(self):
        '''静态人群列表'''
        self.url = self.host + self.path
        data = {"type":"UPLOAD"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #静态人群列表按照名称模糊搜索
    def test_staticCrowdSearchByName(self):
        '''静态人群列表按照名称模糊搜索'''
        self.url = self.host + self.path
        data = {"type":"UPLOAD","name":"是啥"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #静态人群列表按状态模糊搜索-计算中
    def test_staticCrowdSearchByStatus01(self):
        '''静态人群列表按照状态模糊搜索-计算中'''
        self.url = self.host + self.path
        data = {"type":"UPLOAD","name":"是啥","status":"RUN"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    # 静态人群列表按状态模糊搜索-已完成
    def test_staticCrowdSearchByStatus02(self):
        '''静态人群列表按照状态模糊搜索-已完成'''
        self.url = self.host + self.path
        data = {"type":"UPLOAD","name":"是啥","status":"COMPLETE"}
        print(self.url)
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()