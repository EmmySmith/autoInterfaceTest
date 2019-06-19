# -*- coding: utf-8 -*-
# @Time    : 2019-06-18 16:43
# @Author  : Emmy
# @File    : homeProRelationship_test.py


#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
from common.public import *

class CDP_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-report/home/pro/relationship"
        print("----------开始测试----------")


    def test_homeProRelationship(self):
        """客户关系"""
        self.url = self.host + self.path

        data = {
            "startDate": "2019-05-01",
	        "endDate": "2019-05-13"
        }

        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CDP_Interface()