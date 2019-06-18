# -*- coding: utf-8 -*-
# @Time    : 2019-06-13 21:49
# @Author  : Emmy
# @File    : materialCreate_test.py


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
        self.path = "/api/icem-component/micropage/homepage"
        print("----------开始测试----------")


    def test_materialHomepage(self):
        """【素材】设为首页"""
        self.url = self.host + self.path
        data = {
            "pageId":"5d073c35e50665505e1949d1"
        }

        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()

