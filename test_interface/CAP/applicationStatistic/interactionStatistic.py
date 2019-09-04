# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 3:40 PM
# @Author  : Emmy
# @File    : interactionStatistic.py

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
        self.path = "/api/icem-report/interaction/statistic/list?page=0&size=20"


    def test_interactionStatistic(self):
        """互动分析"""
        self.url = self.host + self.path
        print(self.url)
        data={

            }
        response = requests.post(url=self.url,data=json.dumps(data),headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()