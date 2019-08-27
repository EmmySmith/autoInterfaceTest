#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json,time
from common.public import *

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path_list = "/api/icem-activity/market/get/activitys?page=1&size=20"
        self.path_view = "/api/icem-activity/market/activity/list"
        print("----------开始测试----------")


    #营销列表接口
    def test_marketingList(self):
        self.url = self.host + self.path_list
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        data = {"queryTime":nowTime,"page":1,"size":20}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #营销视图列表接口
    def test_marketingViewList(self):
        self.url = self.host + self.path_view
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        data = {"queryTime":nowTime}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0



    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()