# -*- coding: utf-8 -*-
# @Time    : 2019-06-12 20:03
# @Author  : Emmy
# @File    : materialAdd_test.py

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
        self.path = "/api/micropage/material/save"
        print("----------开始测试----------")


    def test_materialSave(self):
        """【素材】新增"""
        self.url = self.host + self.path

        data = {
            "type": "image",
            "title": "7fce0d2b1748734d8c403e976673afa43d2b7ba517141-BZFqXY_fw658.jpeg",
            "group_id": 0,
            "url": "http://geek-icem.oss-cn-beijing.aliyuncs.com/release/1000/material/23a5b020e1954c33af28e5c5876f99c6.jpeg"
        }

        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()
