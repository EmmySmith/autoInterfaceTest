# -*- coding: utf-8 -*-
# @Time    : 2019-06-13 23:13
# @Author  : Emmy
# @File    : materialGroup_test.py


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
        self.path = "/api/icem-wechat/material/wx90d8a37adac76a84/local?type=news&groupId=0&page=0&size=10&query="
        print("----------开始测试----------")


    def test_enterMaterial(self):
        """进入渠道管理"""
        self.url = self.host + self.path


        print(self.url)
        response = requests.get(url=self.url, headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()