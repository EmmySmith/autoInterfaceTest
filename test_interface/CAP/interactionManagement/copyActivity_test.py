# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 5:22 PM
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
        self.path = "/api/icem-interaction/activity/copy"
        print("----------开始测试----------")


    def test_materialDelete(self):
        """复制活动"""
        self.url = self.host + self.path
        data = {
            "id":14
        }

        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0



    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()