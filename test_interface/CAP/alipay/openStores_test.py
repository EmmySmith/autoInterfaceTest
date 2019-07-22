# -*- coding: utf-8 -*-
# @Time    : 2019-07-08 18:02
# @Author  : Emmy
# @File    : openStores_test.py


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
        self.path = "/api/icem-component/stores"
        print("----------开始测试----------")


    def test_materialDelete(self):
        """小程序管理"""
        self.url = self.host + self.path
        data = {
            "channel":"ALIPAY"
        }

        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()

