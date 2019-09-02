# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 11:45 AM
# @Author  : Emmy
# @File    : channelManagement.py

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
        self.path = "/api/icem-interaction/channel/channels?page=0&size=10&sort=createTime,desc"


    def test_channelManagement(self):
        """渠道管理列表"""
        self.url = self.host + self.path
        print(self.url)
        data={
                "sellerId": "1000"
        }
        response = requests.post(url=self.url,data=json.dumps(data),headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()
