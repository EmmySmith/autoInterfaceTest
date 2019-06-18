# -*- coding: utf-8 -*-
# @Time    : 2019-06-13 21:49
# @Author  : Emmy
# @File    : materialBatchDelete.py


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
        self.path = "/api/icem-component/material/batch/delete"
        print("----------开始测试----------")


    def test_materialDelete(self):
        """【素材分组】批量删除"""
        self.url = self.host + self.path
        data = {
            "ids": [103]

        }

        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()

