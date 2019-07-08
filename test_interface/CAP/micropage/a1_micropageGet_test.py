# -*- coding: utf-8 -*-
# @Time    : 2019-06-27 20:50
# @Author  : Emmy
# @File    : a1_micropageGet_test.py


#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json,time
from common.public import *
from common.commonData import *
from test_interface.CAP.micropage.a0_micropageCreate_test import *

class a1_micropageGet_test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-component/micropage/get"
        print("----------开始测试----------")


    def test_materialUpdateTitle(self):
        """查询微页面详情"""
        self.url = self.host + self.path
        data = {
            "pageId": commonData.pageId

        }

        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = a0_micropageCreate_test()
