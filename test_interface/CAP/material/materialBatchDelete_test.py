# -*- coding: utf-8 -*-
# @Time    : 2019-06-13 21:49
# @Author  : Emmy
# @File    : materialBatchDelete_test.py


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
        self.path = "/api/icem-component/material/delete?id=21"
        print("----------开始测试----------")


    def test_materialDelete(self):
        """【素材分组】单个图片删除"""
        self.url = self.host + self.path
        data = {

        }

        print(self.url)
        response = requests.delete(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()

