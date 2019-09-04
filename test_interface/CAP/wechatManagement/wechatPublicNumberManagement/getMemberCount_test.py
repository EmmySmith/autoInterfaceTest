# -*- coding: utf-8 -*-
# @Time    : 2019-07-10 10:05
# @Author  : renming
# @File    : materialGroup_test.py


#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
from common.public import *

class CAP_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-component/home/index?appid=wx90d8a37adac76a84"
        print("----------开始测试----------")

    #获取会员数量，已建页面数量接口
    def test_getMemberCount(self):
        """获取会员数量，已建页面数量接口"""
        self.url = self.host + self.path
        print(self.url)
        response = requests.get(url=self.url,headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()