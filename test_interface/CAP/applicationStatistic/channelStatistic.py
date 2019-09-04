# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 3:38 PM
# @Author  : Emmy
# @File    : channelStatistic.py


#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
import random
from common.public import *


class CAP_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-report/channel/report?page=0&size=10"


    def test_channelStatistic(self):
        """渠道统计"""
        self.url = self.host + self.path
        print(self.url)
        data={
                "terminalName": "WECHAT"
            }
        response = requests.post(url=self.url,data=json.dumps(data),headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()