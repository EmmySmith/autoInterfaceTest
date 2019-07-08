# -*- coding: utf-8 -*-
# @Time    : 2019-06-25 16:30
# @Author  : Emmy
# @File    : homeCrowdCreate_test.py


#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
from common.public import *
import random
import datetime

class CDP_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.random = random.randint(1000,9999)
        self.time = datetime.time()
        self.path = "/api/icem-crowd/home/crowd/create"
        print("----------开始测试----------")


    def test_overviewget(self):
        """保存人群到自定义人群"""
        self.url = self.host + self.path

        data = {
            "type": "all",
            "count": 25457889,
            "columnTitle": "INTERACTIVE_NOPAY",
            "startTime": "2019-06-16 12:00:00",
            "endTime": "2019-06-22 12:00:00",
            "crowdPackageName": str(self.random) + str(self.time) + '是啥'
        }

        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CDP_Interface()
