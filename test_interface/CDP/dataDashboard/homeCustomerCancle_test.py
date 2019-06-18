# -*- coding: utf-8 -*-
# @Time    : 2019-06-18 16:51
# @Author  : Emmy
# @File    : homeCustomerCancle_test.py


#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
from common.public import *

class CDP_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-report/home/customer/cancle"
        print("----------开始测试----------")


    def test_homefreq(self):
        """取消计算"""
        self.url = self.host + self.path

        data = {
            "id": "169"
        }

        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        # assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CDP_Interface()
