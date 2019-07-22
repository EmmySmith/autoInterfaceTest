# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 3:53 PM
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
        self.path = "/interactive/share.html?mode=preview&sellerId=1000&channelCode=guanfang&channelName=%E9%80%9A%E7%94%A8%E6%B8%A0%E9%81%93"
        print("----------开始测试----------")


    def test_materialDelete(self):
        """立即创建弹窗"""
        self.url = self.host + self.path
        data = {
        }

        print(self.url)
        response = requests.get(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)



    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()
