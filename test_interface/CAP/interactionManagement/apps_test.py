# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 4:30 PM
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
        self.path = "/icem-resource/app/channel/apps"
        print("----------开始测试----------")


    def test_materialDelete(self):
        """立即创建--app"""
        self.url = self.host + self.path
        data = {
        }

        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()