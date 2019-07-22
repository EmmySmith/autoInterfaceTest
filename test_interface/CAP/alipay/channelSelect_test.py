# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 2:56 PM
# @Author  : Emmy

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
        self.path = "/api/icem-interaction/channel/channels?page=0&size=10&sort=createTime,desc"
        print("----------开始测试----------")


    def test_materialDelete(self):
        """渠道管理"""
        self.url = self.host + self.path
        data = {
            "sellerId": "1000"
        }

        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()
