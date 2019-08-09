# -*- coding: utf-8 -*-
# @Time    : 2019-06-27 21:22
# @Author  : Emmy
# @File    : a3_micropageHomepage.py


#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import time
from common.public import *
from mysqlHandle.common_mysql import *
from common.commonData import *
from test_interface.CAP.micropage.a2_micropageUpdate import *


class a3_micropageHomepage_test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-component/micropage/homepage"
        print("----------开始测试----------")


    def test_materialUpdateTitle(self):
        """设为主页"""
        self.url = self.host + self.path
        data = {
            "pageId": commonData.pageId
        }
        print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(a0_micropageCreate_test())
    suite.addTest(a1_micropageGet_test())
    suite.addTest(a2_micropageUpdate_test())
    suite.addTest(a3_micropageHomepage_test())
