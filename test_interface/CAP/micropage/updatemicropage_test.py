# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 11:41 AM
# @Author  : Emmy
# @File    : updatemicropage_test.py


#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import time,random
from common.public import *
from common.commonData import *

class CAP_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-component/material/title/update?id=191&title=lslsl&appid=2019031863584181"
        print("----------开始测试----------")


    def test_savemicropage(self):
        """更新图片"""
        self.url = self.host + self.path
        data = {
        }

        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()