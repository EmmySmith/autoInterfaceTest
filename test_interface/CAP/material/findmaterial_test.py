# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 11:34 AM
# @Author  : Emmy
# @File    : findmaterial_test.py


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
        self.path = "/api/icem-component/material/find?type=image&groupId=34&title=&page=0&size=20&appid=2019031863584181"
        print("----------开始测试----------")


    def test_savemicropage(self):
        """查看图片素材分组"""
        self.url = self.host + self.path
        data = {
        }

        print(self.url)
        response = requests.get(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()