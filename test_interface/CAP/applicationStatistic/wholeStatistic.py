# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 3:24 PM
# @Author  : Emmy
# @File    : wholeStatistic.py


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
        self.path = "/api/icem-report/whole/statistic/info"


    def test_wholeStatistic(self):
        """整体统计"""
        self.url = self.host + self.path
        print(self.url)
        data={
                "terminalName": "WECHAT",
                "appId": "wx90d8a37adac76a84",
                "time": "2019-09-03"
            }
        response = requests.post(url=self.url,data=json.dumps(data),headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()