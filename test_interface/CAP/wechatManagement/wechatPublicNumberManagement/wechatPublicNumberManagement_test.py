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
        self.path = "/api/icem-wechat/auth/list"
        print("----------开始测试----------")

    #微信公众号管理
    def test_wechatPublicNumberManagement(self):
        """微信公众号管理"""
        self.url = self.host + self.path
        print(self.url)
        response = requests.get(url=self.url,headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()