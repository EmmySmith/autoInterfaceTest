# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 4:39 PM
# @Author  : Emmy
# @File    : AlipyList_test.py


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
        self.path = "/api/icem-component/alipay/auth/list"
        print("----------开始测试----------")


    def test_AlipayList(self):
        """小程序管理列表显示"""
        self.url = self.host + self.path
        data = {
        }

        print(self.url)
        response = requests.get(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()

