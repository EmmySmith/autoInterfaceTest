# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 3:11 PM
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
        self.path = "/api/icem-component/alipay/mini/2018110562042112/members?role=EXPERIENCER"
        print("----------开始测试----------")


    def test_materialDelete(self):
        """成员管理"""
        self.url = self.host + self.path


        print(self.url)
        response = requests.get(url=self.url, headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0